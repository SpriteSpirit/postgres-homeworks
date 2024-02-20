-- create employees table
CREATE TABLE employees (
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes varchar(500)
);

-- create customers table
CREATE TABLE customers (
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

-- create orders table
CREATE TABLE orders (
	order_id int PRIMARY KEY,
	customer_id varchar(100) NOT NULL,
	employee_id varchar(100),
	order_date date,
	ship_city varchar(100)
);
