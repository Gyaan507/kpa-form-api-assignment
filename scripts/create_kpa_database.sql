-- Create database for KPA forms
CREATE DATABASE kpa_db;

-- Connect to the database
\c kpa_db;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create wheel_specifications table
CREATE TABLE IF NOT EXISTS wheel_specifications (
    id SERIAL PRIMARY KEY,
    form_number VARCHAR(50) UNIQUE NOT NULL,
    submitted_by VARCHAR(50) NOT NULL,
    submitted_date VARCHAR(20) NOT NULL,
    tread_diameter_new VARCHAR(50),
    last_shop_issue_size VARCHAR(50),
    condemning_dia VARCHAR(50),
    wheel_gauge VARCHAR(50),
    variation_same_axle VARCHAR(20),
    variation_same_bogie VARCHAR(20),
    variation_same_coach VARCHAR(20),
    wheel_profile VARCHAR(100),
    intermediate_wwp VARCHAR(50),
    bearing_seat_diameter VARCHAR(50),
    roller_bearing_outer_dia VARCHAR(50),
    roller_bearing_bore_dia VARCHAR(50),
    roller_bearing_width VARCHAR(50),
    axle_box_housing_bore_dia VARCHAR(50),
    wheel_disc_width VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Saved',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create bogie_checksheets table
CREATE TABLE IF NOT EXISTS bogie_checksheets (
    id SERIAL PRIMARY KEY,
    form_number VARCHAR(50) UNIQUE NOT NULL,
    inspection_by VARCHAR(50) NOT NULL,
    inspection_date VARCHAR(20) NOT NULL,
    bogie_details JSONB,
    bogie_checksheet JSONB,
    bmbc_checksheet JSONB,
    status VARCHAR(20) DEFAULT 'Saved',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_wheel_specs_form_number ON wheel_specifications(form_number);
CREATE INDEX idx_wheel_specs_submitted_by ON wheel_specifications(submitted_by);
CREATE INDEX idx_wheel_specs_submitted_date ON wheel_specifications(submitted_date);
CREATE INDEX idx_bogie_form_number ON bogie_checksheets(form_number);
CREATE INDEX idx_bogie_inspection_by ON bogie_checksheets(inspection_by);
CREATE INDEX idx_users_user_id ON users(user_id);
CREATE INDEX idx_users_phone ON users(phone_number);
