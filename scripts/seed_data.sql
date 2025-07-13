-- Insert sample user (password is hashed version of 'to_share@123')
INSERT INTO users (phone_number, password_hash, full_name, email) VALUES 
('7760873976', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBdXwtO5S7ZQvG', 'Test User', 'test@example.com')
ON CONFLICT (phone_number) DO NOTHING;

-- Insert sample form submissions
INSERT INTO form_submissions (user_id, form_type, category, full_name, email, phone_number, address, additional_data, status) VALUES 
(1, 'application', 'personal', 'John Doe', 'john@example.com', '9876543210', '123 Main St, City, State', '{"purpose": "license application", "documents": ["id_proof", "address_proof"]}', 'submitted'),
(1, 'inquiry', 'government', 'Jane Smith', 'jane@example.com', '9876543211', '456 Oak Ave, City, State', '{"subject": "tax inquiry", "priority": "high"}', 'processing'),
(1, 'complaint', 'business', 'Bob Johnson', 'bob@example.com', '9876543212', '789 Pine Rd, City, State', '{"issue": "service complaint", "severity": "medium"}', 'completed')
ON CONFLICT DO NOTHING;
