from fastapi import FastAPI, HTTPException, Depends, status, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn
from datetime import datetime
import json

from database import get_db, engine
from models import Base, WheelSpecification, BogieChecksheet, User
from schemas import (
    WheelSpecificationCreate, WheelSpecificationResponse, 
    WheelSpecCreateResponse, WheelSpecListResponse,
    BogieChecksheetCreate, UserLogin, UserResponse
)
from auth import authenticate_user, create_access_token, get_current_user

# Create tables
print("🔧 Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Database tables created successfully!")

app = FastAPI(
    title="KPA Form Data API",
    description="Railway Operations API for KPA form submissions",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "KPA Form Data API - Railway Operations", 
        "version": "1.0.0",
        "status": "✅ API is running successfully!",
        "endpoints": {
            "docs": "/docs",
            "wheel_specs_post": "/api/forms/wheel-specifications",
            "wheel_specs_get": "/api/forms/wheel-specifications",
            "bogie_checksheet": "/api/forms/bogie-checksheet"
        }
    }

# API 1: POST - Submit Wheel Specifications
@app.post("/api/forms/wheel-specifications", response_model=WheelSpecCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_wheel_specification(
    wheel_spec: WheelSpecificationCreate,
    db: Session = Depends(get_db)
):
    """
    Submit wheel specification form
    
    Creates a new wheel specification entry with all the technical measurements
    and specifications required for railway wheel maintenance.
    """
    try:
        print(f"📝 Creating wheel specification: {wheel_spec.formNumber}")
        
        # Check if form number already exists
        existing_form = db.query(WheelSpecification).filter(
            WheelSpecification.form_number == wheel_spec.formNumber
        ).first()
        
        if existing_form:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Form number {wheel_spec.formNumber} already exists"
            )
        
        # Create new wheel specification
        db_wheel_spec = WheelSpecification(
            form_number=wheel_spec.formNumber,
            submitted_by=wheel_spec.submittedBy,
            submitted_date=wheel_spec.submittedDate,
            tread_diameter_new=wheel_spec.fields.treadDiameterNew,
            last_shop_issue_size=wheel_spec.fields.lastShopIssueSize,
            condemning_dia=wheel_spec.fields.condemningDia,
            wheel_gauge=wheel_spec.fields.wheelGauge,
            variation_same_axle=wheel_spec.fields.variationSameAxle,
            variation_same_bogie=wheel_spec.fields.variationSameBogie,
            variation_same_coach=wheel_spec.fields.variationSameCoach,
            wheel_profile=wheel_spec.fields.wheelProfile,
            intermediate_wwp=wheel_spec.fields.intermediateWWP,
            bearing_seat_diameter=wheel_spec.fields.bearingSeatDiameter,
            roller_bearing_outer_dia=wheel_spec.fields.rollerBearingOuterDia,
            roller_bearing_bore_dia=wheel_spec.fields.rollerBearingBoreDia,
            roller_bearing_width=wheel_spec.fields.rollerBearingWidth,
            axle_box_housing_bore_dia=wheel_spec.fields.axleBoxHousingBoreDia,
            wheel_disc_width=wheel_spec.fields.wheelDiscWidth,
            status="Saved",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        db.add(db_wheel_spec)
        db.commit()
        db.refresh(db_wheel_spec)
        
        print(f"✅ Wheel specification created successfully: {db_wheel_spec.form_number}")
        
        return WheelSpecCreateResponse(
            success=True,
            message="Wheel specification submitted successfully.",
            data={
                "formNumber": db_wheel_spec.form_number,
                "submittedBy": db_wheel_spec.submitted_by,
                "submittedDate": db_wheel_spec.submitted_date,
                "status": db_wheel_spec.status
            }
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error creating wheel specification: {str(e)}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create wheel specification: {str(e)}"
        )

# API 2: GET - Retrieve Wheel Specifications with Filters
@app.get("/api/forms/wheel-specifications", response_model=WheelSpecListResponse)
async def get_wheel_specifications(
    formNumber: Optional[str] = Query(None, description="Filter by form number"),
    submittedBy: Optional[str] = Query(None, description="Filter by submitted by user"),
    submittedDate: Optional[str] = Query(None, description="Filter by submitted date"),
    db: Session = Depends(get_db)
):
    """
    Retrieve wheel specifications with optional filtering
    
    Query parameters:
    - formNumber: Filter by specific form number
    - submittedBy: Filter by user who submitted
    - submittedDate: Filter by submission date
    """
    try:
        print(f"🔍 Fetching wheel specifications with filters: formNumber={formNumber}, submittedBy={submittedBy}, submittedDate={submittedDate}")
        
        query = db.query(WheelSpecification)
        
        # Apply filters
        if formNumber:
            query = query.filter(WheelSpecification.form_number == formNumber)
        if submittedBy:
            query = query.filter(WheelSpecification.submitted_by == submittedBy)
        if submittedDate:
            query = query.filter(WheelSpecification.submitted_date == submittedDate)
        
        specifications = query.all()
        print(f"📊 Found {len(specifications)} wheel specifications")
        
        # Format response data
        response_data = []
        for spec in specifications:
            spec_data = {
                "formNumber": spec.form_number,
                "submittedBy": spec.submitted_by,
                "submittedDate": spec.submitted_date,
                "fields": {
                    "treadDiameterNew": spec.tread_diameter_new,
                    "lastShopIssueSize": spec.last_shop_issue_size,
                    "condemningDia": spec.condemning_dia,
                    "wheelGauge": spec.wheel_gauge,
                    "variationSameAxle": spec.variation_same_axle,
                    "variationSameBogie": spec.variation_same_bogie,
                    "variationSameCoach": spec.variation_same_coach,
                    "wheelProfile": spec.wheel_profile,
                    "intermediateWWP": spec.intermediate_wwp,
                    "bearingSeatDiameter": spec.bearing_seat_diameter,
                    "rollerBearingOuterDia": spec.roller_bearing_outer_dia,
                    "rollerBearingBoreDia": spec.roller_bearing_bore_dia,
                    "rollerBearingWidth": spec.roller_bearing_width,
                    "axleBoxHousingBoreDia": spec.axle_box_housing_bore_dia,
                    "wheelDiscWidth": spec.wheel_disc_width
                },
                "status": spec.status
            }
            response_data.append(spec_data)
        
        return WheelSpecListResponse(
            success=True,
            message="Filtered wheel specification forms fetched successfully.",
            data=response_data
        )
        
    except Exception as e:
        print(f"❌ Error fetching wheel specifications: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve wheel specifications: {str(e)}"
        )

# Bonus API: POST - Submit Bogie Checksheet (Third API for extra credit)
@app.post("/api/forms/bogie-checksheet", status_code=status.HTTP_201_CREATED)
async def create_bogie_checksheet(
    bogie_data: BogieChecksheetCreate,
    db: Session = Depends(get_db)
):
    """
    Submit bogie checksheet form
    
    Creates a new bogie inspection checksheet with detailed component conditions.
    """
    try:
        print(f"📝 Creating bogie checksheet: {bogie_data.formNumber}")
        
        # Check if form number already exists
        existing_form = db.query(BogieChecksheet).filter(
            BogieChecksheet.form_number == bogie_data.formNumber
        ).first()
        
        if existing_form:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Form number {bogie_data.formNumber} already exists"
            )
        
        # Create new bogie checksheet
        db_bogie = BogieChecksheet(
            form_number=bogie_data.formNumber,
            inspection_by=bogie_data.inspectionBy,
            inspection_date=bogie_data.inspectionDate,
            bogie_details=json.dumps(bogie_data.bogieDetails.dict()),
            bogie_checksheet=json.dumps(bogie_data.bogieChecksheet.dict()),
            bmbc_checksheet=json.dumps(bogie_data.bmbcChecksheet.dict()),
            status="Saved",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        db.add(db_bogie)
        db.commit()
        db.refresh(db_bogie)
        
        print(f"✅ Bogie checksheet created successfully: {db_bogie.form_number}")
        
        return {
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": db_bogie.form_number,
                "inspectionBy": db_bogie.inspection_by,
                "inspectionDate": db_bogie.inspection_date,
                "status": db_bogie.status
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error creating bogie checksheet: {str(e)}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create bogie checksheet: {str(e)}"
        )

# Authentication endpoints (for testing)
@app.post("/api/v1/auth/login")
async def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate user with phone number and password
    """
    user = authenticate_user(db, user_credentials.phone_number, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid phone number or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.phone_number})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "user_id": user.user_id,
            "phone_number": user.phone_number,
            "full_name": user.full_name,
            "email": user.email
        }
    }

if __name__ == "__main__":
    print("🚀 Starting KPA Form Data API...")
    print("📍 API will be available at:")
    print("   - http://localhost:8000")
    print("   - http://127.0.0.1:8000")
    print("📚 Documentation at:")
    print("   - http://localhost:8000/docs")
    print("   - http://127.0.0.1:8000/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
