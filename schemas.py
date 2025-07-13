from pydantic import BaseModel, validator
from typing import Optional, Dict, Any
from datetime import datetime

class UserLogin(BaseModel):
    phone_number: str
    password: str

class UserResponse(BaseModel):
    id: int
    user_id: str
    phone_number: str
    full_name: str
    email: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

# Wheel Specification Schemas
class WheelSpecificationFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecificationFields
    
    @validator('formNumber')
    def validate_form_number(cls, v):
        if not v or not v.startswith('WHEEL-'):
            raise ValueError('Form number must start with WHEEL-')
        return v

class WheelSpecificationResponse(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Optional[Dict[str, str]] = None
    status: str = "Saved"
    
    class Config:
        from_attributes = True

# API Response Schemas
class APIResponse(BaseModel):
    success: bool
    message: str
    data: Any

class WheelSpecCreateResponse(BaseModel):
    success: bool = True
    message: str = "Wheel specification submitted successfully."
    data: Dict[str, str]

class WheelSpecListResponse(BaseModel):
    success: bool = True
    message: str = "Filtered wheel specification forms fetched successfully."
    data: list

# Bogie Checksheet Schemas (for future use)
class BogieDetails(BaseModel):
    bogieNo: str
    makerYearBuilt: str
    incomingDivAndDate: str
    deficitComponents: str
    dateOfIOH: str

class BogieChecksheetFields(BaseModel):
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str
    axleGuide: str

class BMBCChecksheetFields(BaseModel):
    cylinderBody: str
    pistonTrunnion: str
    adjustingTube: str
    plungerSpring: str

class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheetFields
    bmbcChecksheet: BMBCChecksheetFields
