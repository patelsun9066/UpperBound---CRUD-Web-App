SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


-- Create Customers Table 

CREATE OR REPLACE TABLE Customers (
	customer_id int NOT NULL AUTO_INCREMENT,
	first_name varchar(200) NOT NULL, 
	last_name varchar(200) NOT NULL, 
	email varchar(250) NOT NULL,
	address varchar(400) NOT NULL,
	phone_number varchar(15) NOT NULL, 
	first_purchase DATE NOT NULL, 
	last_purchase DATE NOT NULL,
	PRIMARY KEY (customer_id),
	UNIQUE(customer_id)
);


-- Create Vendors table 

CREATE OR REPLACE TABLE Vendors (
	vendor_id int NOT NULL AUTO_INCREMENT,
	name varchar(200) NOT NULL, 
	address varchar(400) NOT NULL, 
	contact_name varchar(200) NOT NULL,
	contact_phone_number varchar(15) NOT NULL, 
	contact_email varchar(250) NOT NULL,
	PRIMARY KEY (vendor_id),
	UNIQUE(vendor_id)
);


-- Create Status Codes Table

CREATE OR REPLACE TABLE Status_Codes (
	status_code_id int NOT NULL AUTO_INCREMENT,
	status varchar(150) NOT NULL, 
	PRIMARY KEY (status_code_id),
	UNIQUE(status_code_id)
);


-- Create Sales Table 

CREATE OR REPLACE TABLE Sales (
	sale_id int NOT NULL AUTO_INCREMENT,
	sale_date DATE NOT NULL, 
	shipping_date DATE NOT NULL, 
	customer_id int NOT NULL, 
	status_code_id int,
	PRIMARY KEY (sale_id),
	UNIQUE(sale_id),
	FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE,
	FOREIGN KEY (status_code_id) REFERENCES Status_Codes(status_code_id)
);


-- Create Products Table 

CREATE OR REPLACE TABLE Products (
	product_id int NOT NULL AUTO_INCREMENT,
	name varchar(250) NOT NULL, 
	description varchar(500) NOT NULL, 
	quantity_in_stock int NOT NULL,
	total_dollar_value DECIMAL(19,2) NOT NULL, 
	PRIMARY KEY (product_id),
	UNIQUE(product_id)
);



-- Add Create Purchase Orders table 

CREATE OR REPLACE TABLE Purchase_Orders (
	purchase_order_id int NOT NULL AUTO_INCREMENT,
	purchase_date DATE NOT NULL, 
	delivery_date DATE NOT NULL, 
	vendor_id int NOT NULL,
	PRIMARY KEY (purchase_order_id),
	FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id),
	UNIQUE(purchase_order_id)
);


-- Create Products_Sales table 

CREATE OR REPLACE TABLE Products_Sales (
	product_sale_id int NOT NULL AUTO_INCREMENT,
	product_id int NOT NULL, 
	sale_id int NOT NULL, 
	quantity_sold int NOT NULL, 
	unit_selling_price DECIMAL(19,2) NOT NULL, 
	total_price DECIMAL(19,2) NOT NULL, 
	PRIMARY KEY(product_sale_id),
	UNIQUE(product_sale_id),
	FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,
	FOREIGN KEY (sale_id) REFERENCES Sales(sale_id) ON DELETE CASCADE
);


-- Create Purchase_Orders_Products

CREATE OR REPLACE TABLE Purchase_Orders_Products (
	purchase_order_product_id int NOT NULL AUTO_INCREMENT,
	purchase_order_id int NOT NULL, 
	product_id int NOT NULL,
	purchase_quantity int NOT NULL,
	purchase_price DECIMAL(19,2) NOT NULL,  
	PRIMARY KEY(purchase_order_product_id),
	UNIQUE(purchase_order_product_id),
	FOREIGN KEY(purchase_order_id) REFERENCES Purchase_Orders(purchase_order_id) ON DELETE CASCADE,
	FOREIGN KEY(product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);



-- Insert Sample data into Customers table

INSERT INTO Customers (first_name, last_name, email, address, phone_number, first_purchase, last_purchase)
VALUES
("John", "Doe", "johndoe@gmail.com", "123 Main St, Anytown USA", "555-555-5555", "2021-01-01", "2021-01-01"),
("Jane", "Smith", "janesmith@gmail.com", "456 Elm St, Anytown USA", "555-555-5556", "2021-02-01", "2021-02-01"),
("Bob", "Johnson", "bobjohnson@gmail.com", "789 Oak St, Anytown USA", "555-555-5557", "2021-03-01", "2021-03-01");

-- Insert sample data for Vendors table:

INSERT INTO Vendors (name, address, contact_name, contact_phone_number, contact_email)
VALUES
("ABC Inc", "987 Maple St, Anytown USA", "John Doe", "555-555-5558", "abcinc@gmail.com"),
("XYZ Corp", "654 Pine St, Anytown USA", "Jane Smith", "555-555-5559", "xyzcorp@gmail.com"),
("LMN Enterprises", "321 Cedar St, Anytown USA", "Bob Johnson", "555-555-5560", "lmnenterprises@gmail.com");


-- Insert sample data for Status Codes table:

INSERT INTO Status_Codes (status)
VALUES
("Delivered"),
("In-Transit"),
("Processing-Order");


-- Insert sample data for Sales table:

INSERT INTO Sales (sale_date, shipping_date, customer_id, status_code_id)
VALUES
("2021-01-02", "2021-01-03", 1, 2),
("2021-02-03", "2021-02-04", 2, 1),
("2021-03-04", "2021-03-05", 3, 3);

-- Insert sample data for Products table:

INSERT INTO Products (name, description, quantity_in_stock, total_dollar_value)
VALUES
("Product A", "Description of Product A", 100, 1000.00),
("Product B", "Description of Product B", 200, 2000.00),
("Product C", "Description of Product C", 300, 3000.00);

-- Insert sample data for Purchase_Orders table:

INSERT INTO Purchase_Orders (purchase_date, delivery_date, vendor_id)
VALUES
("2021-01-01", "2021-01-02", 1),
("2021-02-01", "2021-02-02", 2),
("2021-03-01", "2021-03-02", 3);

-- Insert sample data for Purchase_Orders_Products table:

INSERT INTO Purchase_Orders_Products (purchase_order_id, product_id, purchase_quantity, purchase_price)
VALUES
(3,1, 100, 250.00),
(1,2, 1000, 30.00),
(2,3, 10000, 5.00);

-- Insert sample data for Products_Sales table:

INSERT INTO Products_Sales (product_id, sale_id, quantity_sold, unit_selling_price, total_price)
VALUES
(1,3, 10, 350.00, 3500.00 ),
(2,1, 20, 50.00, 1000.00),
(3,2, 30, 10.00, 300.00);


SET FOREIGN_KEY_CHECKS=1;
COMMIT;