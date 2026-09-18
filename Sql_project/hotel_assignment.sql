-- STEP 1: CREATE DATABASE
CREATE DATABASE hotel_assingment;

USE hotel_assingment;


-- STEP 2: CREATE TABLES

-- TABLE 1: CUstomers is here 
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email_id VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- TABLE 2: ROoms table is here
CREATE TABLE rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(8) UNIQUE NOT NULL,
    has_wifi BOOLEAN DEFAULT TRUE,
    has_balcony BOOLEAN DEFAULT FALSE,
    capacity TINYINT NOT NULL,
    rate_per_night DECIMAL(7,2) NOT NULL,
    room_status VARCHAR(15) DEFAULT 'Available'
);

-- TABLE 3: BOOKINGS
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_price DECIMAL(10,2),
    booking_status VARCHAR(20) DEFAULT 'Confirmed',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- TABLE 4: PAYMENTS
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status VARCHAR(20) DEFAULT 'Paid',
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

select * from payments;

-- STEP 3: INSERT SAMPLE DATA

-- CUSTOMERS
INSERT INTO customers (first_name, last_name, email_id, phone_number, address) VALUES
('Rajesh', 'coffee', 'rajesh.coffee@email.com', '+911234567890', '123 Main St, Berlin'),
('Rakesh', 'beniwal', 'rajesh.beni@email.com', '+35987654321', '456 Oak Ave, Munich'),
('Piyush', 'raj', 'raj.piyush@email.com', '+491555555555', '789 Pine Rd, Hamburg'),
('Radha', 'kaur', 'kr.radha@email.com', '+11112223333', '321 Elm St, Frankfurt'),
('Shifali', 'Chauhan', 'shifali.chauhan@email.com', '+919998887777', '654 Cedar Ln, Berlin');

-- ROOMS
INSERT INTO rooms
(room_number, has_wifi, has_balcony, capacity, rate_per_night, room_status)
VALUES
('101', TRUE, FALSE, 1, 80.00, 'Available'),
('102', TRUE, TRUE, 2, 120.00, 'Available'),
('103', TRUE, FALSE, 2, 120.00, 'Occupied'),
('201', TRUE, TRUE, 4, 250.00, 'Available'),
('202', TRUE, TRUE, 2, 180.00, 'Available'),
('301', TRUE, TRUE, 6, 500.00, 'Available');

-- BOOKINGS
INSERT INTO bookings
(customer_id, room_id, check_in_date, check_out_date, total_price, booking_status)
VALUES
(1, 1, '2026-09-15', '2026-09-18', 240.00, 'Confirmed'),
(2, 3, '2026-09-01', '2026-09-05', 480.00, 'Completed'),
(3, 4, '2026-09-20', '2026-09-22', 500.00, 'Confirmed'),
(1, 6, '2026-09-10', '2026-09-15', 2500.00, 'Completed'),
(4, 2, '2026-09-10', '2026-09-12', 240.00, 'Completed'),
(5, 5, '2026-09-01', '2026-09-03', 360.00, 'Completed');

-- PAYMENTS
INSERT INTO payments (booking_id, amount, payment_method, payment_status) VALUES
(1, 240.00, 'Credit Card', 'Paid'),
(2, 480.00, 'PayPal', 'Paid'),
(3, 500.00, 'Credit Card', 'Pending'),
(4, 2500.00, 'Online Banking', 'Paid'),
(5, 240.00, 'Cash', 'Paid'),
(6, 360.00, 'Debit Card', 'Paid');

-- STEP 4: QUERIES - CRUD OPERATIONS

-- 4.1: SELECT (Read)
-- All customers
SELECT * FROM customers;

-- All rooms
SELECT * FROM rooms;

-- All bookings
SELECT * FROM bookings;

-- All payments
SELECT * FROM payments;

-- 4.2: SELECT with WHERE (Filter)

-- Available rooms only
SELECT * FROM rooms WHERE room_status = 'Available';

-- Customer named John
SELECT * FROM customers WHERE first_name = 'Rajesh';

-- Rooms priced over 200
SELECT * FROM rooms WHERE rate_per_night > 200;

-- 4.3: INSERT (Create)

-- Add a new customer
INSERT INTO customers (first_name, last_name, email_id, phone_number, address) 
VALUES ('Rishikesh', 'glass', 'rishi.glass@email.com', '+924445556666', '999 Rose St, Berlin');

-- Add a new room
INSERT INTO rooms (room_number, has_balcony, has_wifi, rate_per_night, capacity, room_status) 
VALUES ('104', true, true, 90.00, 1, 'Available');

-- 4.4: UPDATE
-- Change room 103 status to Available
UPDATE rooms SET room_status = 'Available' WHERE room_number = '103';

-- Update customer email
UPDATE customers SET email_id = 'rajesh.tea@email.com' WHERE customer_id = 1;

-- STEP 5: QUERIES - JOINS

-- 5.1: INNER JOIN - Bookings with customer & room info ----------
SELECT
    b.booking_id,
    c.first_name,
    c.last_name,
    r.room_number,
    r.capacity,
    r.rate_per_night,
    r.room_status,
    b.check_in_date,
    b.check_out_date,
    b.total_price,
    b.booking_status
FROM bookings b
INNER JOIN customers c
    ON b.customer_id = c.customer_id
INNER JOIN rooms r
    ON b.room_id = r.room_id;

-- 5.2: JOIN with Payments 
SELECT 
    b.booking_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_method,
    p.payment_status
FROM bookings b
INNER JOIN customers c ON b.customer_id = c.customer_id
INNER JOIN payments p ON b.booking_id = p.booking_id;

-- 5.3: LEFT JOIN - All customers even without bookings
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    b.booking_id
FROM customers c
LEFT JOIN bookings b ON c.customer_id = b.customer_id;


-- STEP 6: QUERIES - AGGREGATIONS

-- 6.1: COUNT 
-- Total number of customers
SELECT COUNT(*) AS total_customers FROM customers;

-- Total number of bookings
SELECT COUNT(*) AS total_bookings FROM bookings;

-- 6.2: SUM 
-- Total revenue from all bookings
SELECT SUM(total_price) AS total_revenue FROM bookings;

-- Total payment amount
SELECT SUM(amount) AS total_paid FROM payments WHERE payment_status = 'Paid';

--  6.3: AVG
-- Average room price
SELECT AVG(rate_per_night) AS average_price FROM rooms;

-- Average booking value
SELECT AVG(total_price) AS avg_booking_value FROM bookings;

-- 6.4: MAX / MIN
-- Most expensive room
SELECT MAX(rate_per_night) AS most_expensive FROM rooms;

-- Cheapest room
SELECT MIN(rate_per_night) AS cheapest FROM rooms;

-- 6.5 GROUP BY
-- Bookings grouped by room capacity
SELECT
    r.capacity,
    COUNT(b.booking_id) AS total_bookings,
    SUM(b.total_price) AS total_revenue
FROM rooms r
INNER JOIN bookings b
    ON r.room_id = b.room_id
GROUP BY r.capacity;

-- Total amount spent per customer
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(b.booking_id) AS num_bookings,
    SUM(b.total_price) AS total_spent
FROM customers c
INNER JOIN bookings b ON c.customer_id = b.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC;

-- 6.6: HAVING
-- Customers who spent more than 500
SELECT 
    c.first_name,
    c.last_name,
    SUM(b.total_price) AS total_spent
FROM customers c
INNER JOIN bookings b ON c.customer_id = b.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING total_spent > 500;

-- STEP 7: ADDITIONAL BUSINESS QUERIES

-- Find customers with pending payments
SELECT 
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_status
FROM customers c
INNER JOIN bookings b ON c.customer_id = b.customer_id
INNER JOIN payments p ON b.booking_id = p.booking_id
WHERE p.payment_status = 'Pending';

-- Room occupancy report
SELECT 
    room_status,
    COUNT(*) AS num_rooms
FROM rooms
GROUP BY room_status;

-- Most recent bookings
SELECT 
    b.booking_id,
    c.first_name,
    c.last_name,
    b.check_in_date,
    b.booking_status
FROM bookings b
INNER JOIN customers c ON b.customer_id = c.customer_id
ORDER BY b.check_in_date DESC
LIMIT 5;

-- END OF SCRIPT