"""
Script to create sample data in the PostgreSQL database
Run this after starting the application for the first time
"""
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, WheelSpecification, BogieChecksheet
from auth import get_password_hash
import json
from datetime import datetime

def create_sample_data():
    print("Creating sample data for KPA Form API...")
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Create sample user
        existing_user = db.query(User).filter(User.user_id == "user_id_123").first()
        if not existing_user:
            sample_user = User(
                user_id="user_id_123",
                phone_number="7760873976",
                password_hash=get_password_hash("to_share@123"),
                full_name="Railway Inspector",
                email="inspector@railway.com",
                is_active=True
            )
            db.add(sample_user)
            print("Sample user created (user_id_123)")
        else:
            print("Sample user already exists")
        
        # Create sample wheel specification
        existing_wheel = db.query(WheelSpecification).filter(
            WheelSpecification.form_number == "WHEEL-2025-001"
        ).first()
        
        if not existing_wheel:
            sample_wheel = WheelSpecification(
                form_number="WHEEL-2025-001",
                submitted_by="user_id_123",
                submitted_date="2025-07-03",
                tread_diameter_new="915 (900-1000)",
                last_shop_issue_size="837 (800-900)",
                condemning_dia="825 (800-900)",
                wheel_gauge="1600 (+2,-1)",
                variation_same_axle="0.5",
                variation_same_bogie="5",
                variation_same_coach="13",
                wheel_profile="29.4 Flange Thickness",
                intermediate_wwp="20 TO 28",
                bearing_seat_diameter="130.043 TO 130.068",
                roller_bearing_outer_dia="280 (+0.0/-0.035)",
                roller_bearing_bore_dia="130 (+0.0/-0.025)",
                roller_bearing_width="93 (+0/-0.250)",
                axle_box_housing_bore_dia="280 (+0.030/+0.052)",
                wheel_disc_width="127 (+4/-0)",
                status="Saved"
            )
            db.add(sample_wheel)
            print("Sample wheel specification created (WHEEL-2025-001)")
        else:
            print(" Sample wheel specification already exists")
        
        # Create sample bogie checksheet
        existing_bogie = db.query(BogieChecksheet).filter(
            BogieChecksheet.form_number == "BOGIE-2025-001"
        ).first()
        
        if not existing_bogie:
            bogie_details = {
                "bogieNo": "BG1234",
                "makerYearBuilt": "RDSO/2018", 
                "incomingDivAndDate": "NR / 2025-06-25",
                "deficitComponents": "None",
                "dateOfIOH": "2025-07-01"
            }
            
            bogie_checksheet = {
                "bogieFrameCondition": "Good",
                "bolster": "Good", 
                "bolsterSuspensionBracket": "Cracked",
                "lowerSpringSeat": "Good",
                "axleGuide": "Worn"
            }
            
            bmbc_checksheet = {
                "cylinderBody": "WORN OUT",
                "pistonTrunnion": "GOOD",
                "adjustingTube": "DAMAGED", 
                "plungerSpring": "GOOD"
            }
            
            sample_bogie = BogieChecksheet(
                form_number="BOGIE-2025-001",
                inspection_by="user_id_456",
                inspection_date="2025-07-03",
                bogie_details=json.dumps(bogie_details),
                bogie_checksheet=json.dumps(bogie_checksheet),
                bmbc_checksheet=json.dumps(bmbc_checksheet),
                status="Saved"
            )
            db.add(sample_bogie)
            print("Sample bogie checksheet created (BOGIE-2025-001)")
        else:
            print("Sample bogie checksheet already exists")
        
        db.commit()
        print(" Sample data creation completed!")
        print("\n Test Data Available:")
        print("   - User: user_id_123 (phone: 7760873976, password: to_share@123)")
        print("   - Wheel Spec: WHEEL-2025-001")
        print("   - Bogie Checksheet: BOGIE-2025-001")
        
    except Exception as e:
        print(f" Error creating sample data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
