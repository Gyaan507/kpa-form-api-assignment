-- sample user for testing
INSERT INTO users (user_id, phone_number, password_hash, full_name, email) VALUES 
('user_id_123', '7760873976', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBdXwtO5S7ZQvG', 'Railway Inspector', 'inspector@railway.com')
ON CONFLICT (user_id) DO NOTHING;

-- sample wheel specification
INSERT INTO wheel_specifications (
    form_number, submitted_by, submitted_date,
    tread_diameter_new, last_shop_issue_size, condemning_dia, wheel_gauge,
    variation_same_axle, variation_same_bogie, variation_same_coach,
    wheel_profile, intermediate_wwp, bearing_seat_diameter,
    roller_bearing_outer_dia, roller_bearing_bore_dia, roller_bearing_width,
    axle_box_housing_bore_dia, wheel_disc_width, status
) VALUES (
    'WHEEL-2025-001', 'user_id_123', '2025-07-03',
    '915 (900-1000)', '837 (800-900)', '825 (800-900)', '1600 (+2,-1)',
    '0.5', '5', '13',
    '29.4 Flange Thickness', '20 TO 28', '130.043 TO 130.068',
    '280 (+0.0/-0.035)', '130 (+0.0/-0.025)', '93 (+0/-0.250)',
    '280 (+0.030/+0.052)', '127 (+4/-0)', 'Saved'
) ON CONFLICT (form_number) DO NOTHING;

-- sample bogie checksheet
INSERT INTO bogie_checksheets (
    form_number, inspection_by, inspection_date,
    bogie_details, bogie_checksheet, bmbc_checksheet, status
) VALUES (
    'BOGIE-2025-001', 'user_id_456', '2025-07-03',
    '{"bogieNo": "BG1234", "makerYearBuilt": "RDSO/2018", "incomingDivAndDate": "NR / 2025-06-25", "deficitComponents": "None", "dateOfIOH": "2025-07-01"}',
    '{"bogieFrameCondition": "Good", "bolster": "Good", "bolsterSuspensionBracket": "Cracked", "lowerSpringSeat": "Good", "axleGuide": "Worn"}',
    '{"cylinderBody": "WORN OUT", "pistonTrunnion": "GOOD", "adjustingTube": "DAMAGED", "plungerSpring": "GOOD"}',
    'Saved'
) ON CONFLICT (form_number) DO NOTHING;
