INSERT INTO vendors
(vendor_name, contact_email, phone, address, gst_number)
VALUES
('ABC Technologies', 'abc@example.com', '9876543210', 'Bangalore', '29ABCDE1234F1Z5'),
('XYZ Systems', 'xyz@example.com', '9123456780', 'Mysore', '29XYZDE5678G1Z2');

INSERT INTO quotes
(vendor_id, quote_number, quote_date, total_amount, payment_terms, lead_time_days, validity_days)
VALUES
(1, 'Q-001', CURRENT_DATE, 85000.00, 'Net-30', 7, 30),
(1, 'Q-002', CURRENT_DATE, 82000.00, 'Net-15', 10, 30),
(2, 'Q-003', CURRENT_DATE, 87500.00, 'Net-30', 5, 45);
