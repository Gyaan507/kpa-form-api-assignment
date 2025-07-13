# KPA Form Data API - Railway Operations Backend

## 📋 Project Overview
A FastAPI-based backend application implementing **two specific APIs** from the KPA Railway Operations Postman collection for railway form data management.

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   \`\`\`bash
   git clone <your-github-repo-url>
   cd kpa-form-api
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Setup PostgreSQL Database**
   \`\`\`bash
   # Create database
   createdb kpa_db
   
   # Run setup scripts
   psql -d kpa_db -f scripts/create_kpa_database.sql
   psql -d kpa_db -f scripts/seed_kpa_data.sql
   \`\`\`

4. **Configure environment variables**
   \`\`\`bash
   # Update .env file with your database credentials
   DATABASE_URL=postgresql://postgres:your_password@localhost/kpa_db
   SECRET_KEY=your-secret-key-here
   \`\`\`

5. **Create sample data**
   \`\`\`bash
   python create_sample_data.py
   \`\`\`

6. **Run the application**
   \`\`\`bash
   python main.py
   \`\`\`

7. **Access the API**
   - API Base URL: http://localhost:8000
   - Interactive Documentation: http://localhost:8000/docs

## 🛠️ Tech Stack Used

| Component | Technology | Version |
|-----------|------------|---------|
| **Framework** | FastAPI | 0.104.1 |
| **Database** | PostgreSQL | Latest |
| **ORM** | SQLAlchemy | 2.0.23 |
| **Validation** | Pydantic | 2.5.0 |
| **Authentication** | JWT (python-jose) | 3.3.0 |
| **Password Hashing** | bcrypt (passlib) | 1.7.4 |
| **Server** | Uvicorn | 0.24.0 |
| **Environment Config** | python-dotenv | 1.0.0 |

## 🔧 Implemented APIs

### 1. POST /api/forms/wheel-specifications
**Description**: Submit wheel specification forms with detailed technical measurements for railway wheel maintenance.

**Request Body**:
\`\`\`json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
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

**Response**: 201 Created with success confirmation and form details.

### 2. GET /api/forms/wheel-specifications
**Description**: Retrieve wheel specifications with optional filtering capabilities.

**Query Parameters**:
- `formNumber`: Filter by specific form number
- `submittedBy`: Filter by user who submitted
- `submittedDate`: Filter by submission date

**Response**: 200 OK with array of matching wheel specification forms.

## ✨ Key Features Implemented

### Core Features
- ✅ **Two APIs** exactly matching Postman collection structure
- ✅ **PostgreSQL integration** with proper database schema
- ✅ **Input validation** using Pydantic models with custom validators
- ✅ **Error handling** with appropriate HTTP status codes
- ✅ **Auto-generated documentation** via Swagger/OpenAPI

### Bonus Features
- ✅ **Environment-based configuration** using .env files
- ✅ **JWT Authentication** with secure password hashing
- ✅ **Third API** (bogie checksheet) for extra credit
- ✅ **Comprehensive validation** for all input fields
- ✅ **Database indexing** for optimal performance
- ✅ **CORS middleware** for cross-origin requests

## 🔒 Security Features
- JWT-based authentication
- Password hashing using bcrypt
- Input validation and sanitization
- SQL injection prevention via ORM
- Environment-based secret management

## 📊 Database Schema
- **users**: User authentication and profile data
- **wheel_specifications**: Wheel specification form data with all technical measurements
- **bogie_checksheets**: Bogie inspection form data (bonus feature)

## 🧪 Testing
- **Postman Collection**: Complete collection with working examples
- **Sample Data**: Pre-loaded test data for immediate testing
- **Interactive Docs**: Swagger UI for live API testing
- **Test Scripts**: Automated testing scripts included

## ⚠️ Limitations and Assumptions

### Assumptions Made
1. **Form Number Format**: Accepts flexible form number formats (not strictly WHEEL- prefix for testing)
2. **Date Format**: Accepts date as string format as per Postman collection
3. **User Authentication**: Simplified user model for assignment scope
4. **Database**: Assumes PostgreSQL is available and configured

### Known Limitations
1. **File Upload**: Not implemented (not required in Postman collection)
2. **Advanced Filtering**: Basic filtering implemented as per requirements
3. **Pagination**: Not implemented for GET endpoints
4. **Rate Limiting**: Not implemented for assignment scope

## 📞 Support
- **Assignment Contact**: kumargyan89@gmail.com, 8434392525
- **Documentation**: Available at http://localhost:8000/docs when running



