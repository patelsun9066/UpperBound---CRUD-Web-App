----------------------------------

-- Get all customers 
Select * from Customers; 

-- Create a new customer 
INSERT INTO Customers (first_name, last_name, email, address, phone_number, first_purchase, last_purchase)
VALUES (:first_nameInput, :last_nameInput, :emailInput, :addressInput, :phone_numberInput, :first_purchaseInput, :last_purchaseInput);

-- Update customers data 
Select customer_id, first_name, last_name, email, address, phone_number, first_purchase, last_purchase from Customers 
WHERE customer_id = :customer_ID_selected_from_customers_page;

Update Customers SET first_name = :first_nameInput, last_name = :last_nameInput, email = :emailInput, address = :addressInput, phone_number = :phone_numberInput, first_purchase = :first_purchaseInput, last_purchase = :last_purchaseInput
WHERE customer_id = :customer_ID_selected_from_update_form;

-- Delete a customer
DELETE FROM Customers WHERE customer_id = :customer_id_selected_from_browse_customers_page;

---------------------------------------

-- Get All Vendors 
Select * from Vendors; 

-- Insert into Vendors Table
INSERT INTO Vendors (name, address, contact_name, contact_phone_number, contact_email)
VALUES (:nameInput, :addressInput, :contact_nameInput, :contact_phone_numberInput, :contact_emailInput);

-- Update Vendors Table
Select vendor_id, name, address, contact_name, contact_phone_number, contact_email from Vendors
WHERE vendor_id = :vendor_ID_selected_from_vendors_page;

Update Vendors SET name = :nameInput, address = :addressInput, contact_name = :contact_nameInput, contact_phone_number = :contact_phone_numberInput, contact_email = :contact_emailInput
WHERE vendor_id = :vendor_ID_selected_from_update_form;

-------------------------------------------------

-- Get all Purchase_Orders 
SELECT purchase_order_id, purchase_date, delivery_date, Vendors.name as vendor_name FROM Purchase_Orders INNER JOIN Vendors ON Purchase_Orders.vendor_id = Vendors.vendor_id;

-- Insert into Purchase Orders Table
INSERT INTO Purchase_Orders (purchase_date, delivery_date, vendor_id)
VALUES (:purchase_dateInput, :delivery_dateInput, :vendor_id_from_dropdown_Input);

-- Update Purchase Orders Table
SELECT purchase_order_id, purchase_date, delivery_date, Vendors.vendor_id as vendor_id, Vendors.name as vendor_name FROM Purchase_Orders INNER JOIN Vendors ON Purchase_Orders.vendor_id = Vendors.vendor_id
WHERE purchase_order_id = :purchase_order_ID_selected_from_purchase_orders_page;

Update Purchase_Orders SET purchase_date = :purchase_dateInput, delivery_date = :delivery_dateInput, vendor_id = :vendor_id_from_dropdown_Input
WHERE purchase_order_id = :purchase_order_ID_selected_from_update_form;

-- Delete From a Purchase Order 
DELETE FROM Purchase_Orders WHERE purchase_order_id = :purchase_order_id_selected_from_browse_purchase_orders_page;

------------------------------------------------------

-- Get all Products 
Select * From Products;

-- Insert into Products Table
INSERT INTO Products (name, description, quantity_in_stock, total_dollar_value)
VALUES (:nameInput, :descriptionInput, :quantity_in_stockInput, :total_dollar_valueInput);

-- Update Products Table
Select product_id, name, description, quantity_in_stock, total_dollar_value from Products
WHERE product_id = :product_ID_selected_from_products_page;

Update Products SET name = :nameInput, description = :descriptionInput, quantity_in_stock = :quantity_in_stockInput, total_dollar_value = :total_dollar_valueInput
WHERE product_id = :product_ID_selected_from_update_form;

-----------------------------

-- Get All Sales 

SELECT sale_id, sale_date, shipping_date, CONCAT(Customers.first_name,' ', Customers.last_name) as customer_full_name, Status_Codes.status as status FROM Sales INNER JOIN Customers ON Sales.customer_id = Customers.customer_id INNER JOIN Status_Codes ON Sales.status_code_id = Status_Codes.status_code_id;

-- Insert into Sales Table
INSERT INTO Sales (sale_date, shipping_date, customer_id, status_code_id)
VALUES (:sale_dateInput, :shipping_dateInput, :customer_idInputDropDown, :status_code_idInputDropDown);

-- Update Sales Table
SELECT sale_id, sale_date, shipping_date, Customers.customer_id, Status_Codes.status_code_id, CONCAT(Customers.first_name,' ', Customers.last_name) as customer_full_name, Status_Codes.status as status FROM Sales INNER JOIN Customers ON Sales.customer_id = Customers.customer_id INNER JOIN Status_Codes ON Sales.status_code_id = Status_Codes.status_code_id 
WHERE sale_id =:sale_ID_selected_from_sales_page;

Update Sales SET sale_date = :sale_dateInput, shipping_date = :shipping_dateInput, customer_id = :customer_idInputDropDown, status_code_id = :status_code_idInputDropDown
WHERE sale_id = :sale_ID_selected_from_update_form;

---------------------------------------------

-- Get All Products_Sales 
SELECT product_sale_id, Products.name as product_name, Sales.sale_date as sale_date, quantity_sold, unit_selling_price, total_price FROM Products_Sales INNER JOIN Products ON Products_Sales.product_id = Products.product_id INNER JOIN Sales ON Products_Sales.sale_id = Sales.sale_id;

-- Insert into Products_Sales Table
INSERT INTO Products_Sales (product_id, sale_id, quantity_sold, unit_selling_price, total_price)
VALUES (:product_idInputDropdown, :sale_idInputDropDown, :quantity_soldInput, :unit_selling_priceInput, :total_priceInput);

-- Update Products_Sales Table
SELECT product_sale_id, Products.name as product_name, Sales.sale_date as sale_date, quantity_sold, unit_selling_price, total_price FROM Products_Sales INNER JOIN Products ON Products_Sales.product_id = Products.product_id INNER JOIN Sales ON Products_Sales.sale_id = Sales.sale_id
WHERE product_sale_id = :product_sale_ID_selected_from_products_sales_page;

Update Products_Sales SET product_id = :product_idInputDropdown, sale_id = :sale_idInputDropdown, quantity_sold = :quantity_soldInput, unit_selling_price = :unit_selling_priceInput, total_price = :total_priceInput
WHERE product_sale_id = :product_sale_ID_selected_from_update_form;

-----------------------------------------------

-- Get all Purchase_Orders_Products Table 
SELECT purchase_order_product_id, Purchase_Orders.purchase_date, Products.name as product_name, purchase_quantity, purchase_price From Purchase_Orders_Products INNER JOIN Purchase_Orders ON Purchase_Orders.purchase_order_id = Purchase_Orders_Products.purchase_order_id INNER JOIN Products ON Products.product_id = Purchase_Orders_Products.product_id;

-- Insert into Purchase_Orders_Products Table
INSERT INTO Purchase_Orders_Products (purchase_order_id, product_id, purchase_quantity, purchase_price)
VALUES (:purchase_order_idInputDropdown, :product_idInputDropdown, :purchase_quantityInput, :purchase_priceInput);

-- Update Purchase_Orders_Products Table
SELECT purchase_order_product_id, Purchase_Orders.purchase_order_id as purchase_order_id, Products.product_id as product_id, Purchase_Orders.purchase_date, Products.name as product_name, purchase_quantity, purchase_price From Purchase_Orders_Products INNER JOIN Purchase_Orders ON Purchase_Orders.purchase_order_id = Purchase_Orders_Products.purchase_order_id INNER JOIN Products ON Products.product_id = Purchase_Orders_Products.product_id
WHERE purchase_order_product_id = :purchase_order_product_ID_selected_from_purchase_orders_products_page;

Update Purchase_Orders_Products SET purchase_order_id = :purchase_order_idInputDropdown, product_id = :product_idInputDropdown, purchase_quantity = :purchase_quantityInput, purchase_price = :purchase_priceInput
WHERE purchase_order_product_id = :purchase_order_product_ID_selected_from_update_form;

-- Delete From a Purchase_Orders_Products Table 
DELETE FROM Purchase_Orders_Products WHERE purchase_order_product_id = :purchase_order_product_id_selected_from_browse_purchase_orders_products_page;

-----------------------------------------------------------------------

-- Get all status Codes 
Select * from Status_Codes;

-- Insert into Status Codes Table
INSERT INTO Status_Codes (status)
VALUES (:statusInput);

------------------------------------------------------

-- SQL statements to populate Dropdown Boxes.

-- get all vendor ids and names to populate the vendor id dropdown in Purchase Orders
SELECT vendor_id, name FROM Vendors;

-- get all customer ids and names to populate the customer id dropdown in Sales
SELECT customer_id, CONCAT(Customers.first_name,' ', Customers.last_name) as customer_full_name FROM Customers;

-- get all status code ids and status to populate the status code id dropdown in Sales
SELECT status_code_id, status FROM Status_Codes;

-- get all purchase order ids to populate the purchase order id dropdown in Purchase_Orders_Products
SELECT purchase_order_id, purchase_date FROM Purchase_Orders;

-- get all product ids to populate the product id dropdown in Purchase_Orders_Products
SELECT product_id, name FROM Products;

-- get all product ids to populate the product id dropdown in Product_Sales
SELECT product_id, name FROM Products;

-- get all sale ids to populate the sale id dropdown in Product_Sales
SELECT sale_id, sale_date FROM Sales;