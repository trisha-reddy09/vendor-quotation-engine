CREATE TABLE vendors ( 
id SERIAL PRIMARY KEY, 
vendor_name VARCHAR(150) NOT NULL, 
contact_email VARCHAR(255), 
phone VARCHAR(20), 
address TEXT, 
gst_number VARCHAR(20), 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 
CREATE TABLE quotes ( 
id SERIAL PRIMARY KEY, 
vendor_id INTEGER NOT NULL, 
quote_number VARCHAR(100) NOT NULL, 
quote_date DATE, 
total_amount DECIMAL(12,2), 
payment_terms VARCHAR(50), 
lead_time_days INTEGER, 
validity_days INTEGER, 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
CONSTRAINT fk_quotes_vendor 
FOREIGN KEY (vendor_id) 
REFERENCES vendors(id) 
);