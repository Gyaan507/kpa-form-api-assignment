# KPA Form Data API - Railway Operations

A FastAPI-based backend application implementing the exact KPA form submission APIs for railway operations management.

## 🚀 Implemented APIs

### 1. POST /api/forms/wheel-specifications
- **Purpose**: Submit wheel specification forms with technical measurements
- **Request Body**: Form number, submitted by, date, and detailed wheel measurements
- **Response**: Success confirmation with form details and "Saved" status
- **Validation**: Form number must start with "WHEEL-", all measurements required

### 2. GET /api/forms/wheel-specifications  
- **Purpose**: Retrieve wheel specifications with optional filtering
- **Query Parameters**: formNumber, submittedBy, submittedDate
- **Response**: Array of matching wheel specification forms
- **Features**: Supports filtering by any combination of parameters

### 3. POST /api/forms/bogie-checksheet (Bonus)
- **Purpose**: Submit bogie inspection checksheet forms
- **Request Body**: Inspection details, bogie details, checksheet data
- **Response**: Success confirmation with inspection details

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.104.1
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Validation**: Pydantic models matching exact API structure
- **Documentation**: Auto-generated Swagger/OpenAPI docs
- **Environment**: python-dotenv for configuration

## 📋 Quick Setup

### 1. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Setup PostgreSQL Database
\`\`\`bash
# Create database
createdb kpa_db

# Run setup scripts
psql -d kpa_db -f scripts/create_kpa_database.sql
psql -d kpa_db -f scripts/seed_kpa_data.sql
\`\`\`

### 3. Configure Environment
\`\`\`bash
cp .env.example .env
# Update DATABASE_URL in .env file
\`\`\`

### 4. Run Application
\`\`\`bash
python main.py
# API available at: http://localhost:8000
# Docs available at: http://localhost:8000/docs
\`\`\`

## 📝 API Testing

### Test Data Examples

#### Wheel Specification Submission:
\`\`\`json
{
  "formNumber": "WHEEL-2025-002",
  "submittedBy": "user_id_123", 
  "submittedDate": "2025-07-13",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5", 
    "variationSameCoach": "13",
    "wheelProfile": "29.4 Flange Thickness",
    "intermediateWWP": "20 TO 28",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "wheelDiscWidth": "127 (+4/-0)"
  }
}
\`\`\`

#### Query Examples:
\`\`\`bash
# Get all wheel specifications
GET /api/forms/wheel-specifications

# Get specific form
GET /api/forms/wheel-specifications?formNumber=WHEEL-2025-001

# Get by user and date
GET /api/forms/wheel-specifications?submittedBy=user_id_123&submittedDate=2025-07-03
\`\`\`

## 🔍 API Response Format

All APIs follow the exact response structure from the Postman collection:

\`\`\`json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": { /* response data */ }
}
\`\`\`

## 📊 Database Schema

### wheel_specifications table:
- form_number (unique identifier)
- submitted_by (user reference)
- submitted_date (submission date)
- All wheel measurement fields
- status (default: "Saved")
- timestamps

### bogie_checksheets table:
- form_number (unique identifier)  
- inspection_by (inspector reference)
- inspection_date (inspection date)
- bogie_details (JSON)
- bogie_checksheet (JSON)
- bmbc_checksheet (JSON)
- status (default: "Saved")

## ✅ Assignment Completion

- ✅ **Two APIs implemented**: POST and GET wheel-specifications
- ✅ **Exact API structure**: Matches Postman collection exactly
- ✅ **PostgreSQL database**: Proper schema and relationships
- ✅ **Input validation**: Pydantic models with validation rules
- ✅ **Error handling**: Comprehensive error responses
- ✅ **Documentation**: Auto-generated Swagger docs
- ✅ **Postman collection**: Updated with working endpoints
- ✅ **Environment config**: .env file support
- ✅ **Bonus features**: Third API, comprehensive validation

## 🚀 Deployment Ready

The application is production-ready with:
- Environment-based configuration
- Proper error handling and logging
- Database connection pooling
- CORS middleware
- Input validation and sanitization
- Comprehensive API documentation

## 📞 Support

For questions or issues: contact@suvidhaen.com

**Assignment Status: COMPLETE ✅**
