from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), unique=True, index=True, nullable=False)  # user_id_123 format
    phone_number = Column(String(15), unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String(50), unique=True, index=True, nullable=False)
    submitted_by = Column(String(50), nullable=False)  # user_id reference
    submitted_date = Column(String(20), nullable=False)  # Date as string to match API
    
    # Wheel specification fields
    tread_diameter_new = Column(String(50))
    last_shop_issue_size = Column(String(50))
    condemning_dia = Column(String(50))
    wheel_gauge = Column(String(50))
    variation_same_axle = Column(String(20))
    variation_same_bogie = Column(String(20))
    variation_same_coach = Column(String(20))
    wheel_profile = Column(String(100))
    intermediate_wwp = Column(String(50))
    bearing_seat_diameter = Column(String(50))
    roller_bearing_outer_dia = Column(String(50))
    roller_bearing_bore_dia = Column(String(50))
    roller_bearing_width = Column(String(50))
    axle_box_housing_bore_dia = Column(String(50))
    wheel_disc_width = Column(String(50))
    
    status = Column(String(20), default="Saved")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheets"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String(50), unique=True, index=True, nullable=False)
    inspection_by = Column(String(50), nullable=False)
    inspection_date = Column(String(20), nullable=False)
    
    # Bogie details as JSON
    bogie_details = Column(JSON)
    bogie_checksheet = Column(JSON)
    bmbc_checksheet = Column(JSON)
    
    status = Column(String(20), default="Saved")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
