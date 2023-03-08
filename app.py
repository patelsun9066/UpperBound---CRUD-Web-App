# Citation for the following app.py file:
# Date: 3/02/2023
# Adapted from / Based on: Flask Starter App guide shared from course learning materials.
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app


from flask import Flask, render_template, json, redirect
import os
import database.db_connector as db
from flask import request
from flask_mysqldb import MySQL
from dotenv import load_dotenv, find_dotenv

# Configuration

app = Flask(__name__)
#db_connection = db.connect_to_database()

app.config["MYSQL_HOST"] = os.environ.get("340DBHOST")
app.config["MYSQL_USER"] = os.environ.get("340DBUSER")
app.config["MYSQL_PASSWORD"] = os.environ.get("340DBPW")
app.config["MYSQL_DB"] = os.environ.get("340DBUSER")
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Routes 

@app.route('/')
def root():
    return render_template("main.j2")

# ---------------------------------------------------------------------------------------------------------------------------------------#
# Customers Page Routes - Browse, Add, Update and Delete

@app.route('/Customers', methods=["POST", "GET"])
def Customers_page():

    if request.method == "GET":
        # SQL query to grab all customers in Customers Database
        query = "SELECT * FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("Customers.j2", data=data)

    if request.method == "POST":
        # Fires off if the user presses Add Customer Button
        if request.form.get("Add_Customer"):
            # grab customer form inputs
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            address = request.form["address"]
            phone_number = request.form["phone_number"]
            first_purchase = request.form["first_purchase"]
            last_purchase = request.form["last_purchase"]
            
            # no null inputs allowed
            query = "INSERT INTO Customers (first_name, last_name, email, address, phone_number, first_purchase, last_purchase) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, address, phone_number, first_purchase, last_purchase))
            mysql.connection.commit()      

            # redirect back to people page
            return redirect("/Customers")


# route for update functionality, updating the attributes of a customer in Customers
# similar to our delete route, we want to the pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/Update_Customer/<int:customer_id>", methods=["POST", "GET"])
def update_customer(customer_id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "Select customer_id, first_name, last_name, email, address, phone_number, first_purchase, last_purchase from Customers WHERE customer_id = %s;" % (customer_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render Update_Customer page passing our query data
        return render_template("Update_Customer.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Update_Customer"):
            # grab user form inputs
            customer_id = request.form["customer_id"]
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            address = request.form["address"]
            phone_number = request.form["phone_number"]
            first_purchase = request.form["first_purchase"]
            last_purchase = request.form["last_purchase"]

            query = "Update Customers SET first_name = %s, last_name = %s, email = %s, address = %s, phone_number = %s, first_purchase = %s, last_purchase = %s WHERE customer_id = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, address, phone_number, first_purchase, last_purchase, customer_id))
            mysql.connection.commit()

            # redirect back to Customers page after we execute the update query
            return redirect("/Customers")


# route for delete functionality, deleting a customer from Customers,
# we want to pass the 'id' value of that customer on button click (see HTML) via the route
@app.route("/Delete_Customer/<int:customer_id>")
def delete_customer(customer_id):
    # mySQL query to delete the customer with our passed id
    query = "DELETE FROM Customers WHERE customer_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (customer_id,))
    mysql.connection.commit()

    # redirect back to customers page
    return redirect("/Customers")

# ---------------------------------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------------------------------#
# Vendors Page Routes - Browse, Add, and Update

@app.route('/Vendors', methods=["POST", "GET"])
def Vendors_page():

    if request.method == "GET":
        # SQL query to grab all Vendors in Vendors Database
        query = "SELECT * FROM Vendors;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("Vendors.j2", data=data)


    if request.method == "POST":
        # Fires off if the user presses Add Vendor Button
        if request.form.get("Add_Vendor"):
            # grab customer form inputs
            name = request.form["name"]
            address = request.form["address"]
            contact_name = request.form["contact_name"]
            contact_phone_number = request.form["contact_phone_number"]
            contact_email = request.form["contact_email"]

            # no null inputs allowed
            query = "INSERT INTO Vendors (name, address, contact_name, contact_phone_number, contact_email) VALUES (%s, %s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, address, contact_name, contact_phone_number, contact_email))
            mysql.connection.commit()      

            # redirect back to vendors page
            return redirect("/Vendors")


# route for update functionality, updating the attributes of a vendor in Vendors
# similar to our delete route, we want to the pass the 'id' value of that vendor on button click (see HTML) via the route
@app.route("/Update_Vendor/<int:vendor_id>", methods=["POST", "GET"])
def update_vendor(vendor_id):
    if request.method == "GET":
        # mySQL query to grab the info of the vendor with our passed id
        query = "Select vendor_id, name, address, contact_name, contact_phone_number, contact_email from Vendors WHERE vendor_id = %s;" % (vendor_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render Update_Customer page passing our query data
        return render_template("Update_Vendor.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Vendor' button
        if request.form.get("Update_Vendor"):
            # grab user form inputs
            vendor_id = request.form["vendor_id"]
            name = request.form["name"]
            address = request.form["address"]
            contact_name = request.form["contact_name"]
            contact_phone_number = request.form["contact_phone_number"]
            contact_email = request.form["contact_email"]

            query = "Update Vendors SET name = %s, address = %s, contact_name = %s, contact_phone_number = %s, contact_email = %s WHERE vendor_id = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, address, contact_name, contact_phone_number, contact_email, vendor_id))
            mysql.connection.commit()

            # redirect back to Vendors page after we execute the update query
            return redirect("/Vendors")

# ---------------------------------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------------------------------#
# Purchase Orders Page Routes - Browse, Add, Delete and Update

@app.route('/Purchase_Orders', methods=["POST", "GET"])
def Purchase_Orders_page():

    if request.method == "GET":
        # SQL query to grab all Purchase Orders in PO Database
        query = "SELECT purchase_order_id, purchase_date, delivery_date, Vendors.name as vendor_name FROM Purchase_Orders INNER JOIN Vendors ON Purchase_Orders.vendor_id = Vendors.vendor_id;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab vendor id/name data for our dropdown
        query2 = "SELECT vendor_id, name FROM Vendors;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        vendors = cur.fetchall()

        return render_template("Purchase_Orders.j2", data=data, vendors=vendors)

    if request.method == "POST":
        # Fires off if the user presses Add purchase order Button
        if request.form.get("Add_Purchase_Order"):
            # grab purchase orders form inputs
            purchase_date = request.form["purchase_date"]
            delivery_date = request.form["delivery_date"]
            vendor_id = request.form["vendor_id"]

            # no null inputs allowed
            query = "INSERT INTO Purchase_Orders (purchase_date, delivery_date, vendor_id) VALUES (%s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (purchase_date, delivery_date, vendor_id))
            mysql.connection.commit()      

            # redirect back to vendors page
            return redirect("/Purchase_Orders")

# route for update functionality, updating the attributes of a PO in Purchase Orders
@app.route("/Update_Purchase_Order/<int:purchase_order_id>", methods=["POST", "GET"])
def update_purchase_order(purchase_order_id):
    if request.method == "GET":
        # mySQL query to grab the info of the purchase order with our passed id
        query = "SELECT purchase_order_id, purchase_date, delivery_date, Vendors.vendor_id as vendor_id, Vendors.name as vendor_name FROM Purchase_Orders INNER JOIN Vendors ON Purchase_Orders.vendor_id = Vendors.vendor_id WHERE purchase_order_id = %s;" % (purchase_order_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # mySQL query to grab vendor id/name data for our dropdown
        query2 = "SELECT vendor_id, name FROM Vendors;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        vendors = cur.fetchall()

        # render Update_Customer page passing our query data
        return render_template("Update_Purchase_Order.j2", data=data, vendors=vendors)

    if request.method == "POST":
        # fire off if user clicks the 'Edit Purchase Order' button
        if request.form.get("Update_Purchase_Order"):
            # grab user form inputs
            purchase_order_id = request.form["purchase_order_id"]
            purchase_date = request.form["purchase_date"]
            delivery_date = request.form["delivery_date"]
            vendor_id = request.form["vendor_id"]

            query = "Update Purchase_Orders SET purchase_date = %s, delivery_date = %s, vendor_id = %s WHERE purchase_order_id = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (purchase_date, delivery_date, vendor_id, purchase_order_id))
            mysql.connection.commit()

            # redirect back to Vendors page after we execute the update query
            return redirect("/Purchase_Orders")

# route for delete functionality, deleting a purchase order from Purchase Orders,
@app.route("/Delete_Purchase_Order/<int:purchase_order_id>")
def delete_purchase_order(purchase_order_id):
    # mySQL query to delete the customer with our passed id
    query = "DELETE FROM Purchase_Orders WHERE purchase_order_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (purchase_order_id,))
    mysql.connection.commit()

    # redirect back to customers page
    return redirect("/Purchase_Orders")

# ---------------------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------------------------#
# Products Page Routes - Browse, Add, and Update

@app.route('/Products', methods=["POST", "GET"])
def Products_page():

    if request.method == "GET":
        # SQL query to grab all Products in Products Database
        query = "SELECT * FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("Products.j2", data=data)


    if request.method == "POST":
        # Fires off if the user presses Add Product Button
        if request.form.get("Add_Product"):
            # grab customer form inputs
            name = request.form["name"]
            description = request.form["description"]
            quantity_in_stock = request.form["quantity_in_stock"]
            total_dollar_value = request.form["total_dollar_value"]

            # no null inputs allowed
            query = "INSERT INTO Products (name, description, quantity_in_stock, total_dollar_value) VALUES (%s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, description, quantity_in_stock, total_dollar_value))
            mysql.connection.commit()      

            # redirect back to products page
            return redirect("/Products")


# route for update functionality, updating the attributes of a product in Products

@app.route("/Update_Product/<int:product_id>", methods=["POST", "GET"])
def update_product(product_id):
    if request.method == "GET":
        # mySQL query to grab the info of the product with our passed id
        query = "Select product_id, name, description, quantity_in_stock, total_dollar_value from Products WHERE product_id = %s;" % (product_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render Update_Customer page passing our query data
        return render_template("Update_Product.j2", data=data)

    if request.method == "POST":
        # fire off if user clicks the 'Edit Product' button
        if request.form.get("Update_Product"):
            # grab user form inputs
            product_id = request.form["product_id"]
            name = request.form["name"]
            description = request.form["description"]
            quantity_in_stock = request.form["quantity_in_stock"]
            total_dollar_value = request.form["total_dollar_value"]

            query = "Update Products SET name = %s, description = %s, quantity_in_stock = %s, total_dollar_value = %s WHERE product_id = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (name, description, quantity_in_stock, total_dollar_value, product_id))
            mysql.connection.commit()

            # redirect back to Products page after we execute the update query
            return redirect("/Products")

# ---------------------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------------------------#
# Sales Page Routes - Browse, Add, and Update

@app.route('/Sales', methods=["POST", "GET"])
def Sales_page():

    if request.method == "GET":
        # SQL query to grab all sales in Sales Database
        #query = "SELECT * FROM Sales;"
        query = "SELECT sale_id, sale_date, shipping_date, CONCAT(Customers.first_name,' ', Customers.last_name) as customer_full_name, Status_Codes.status as status FROM Sales INNER JOIN Customers ON Sales.customer_id = Customers.customer_id LEFT JOIN Status_Codes ON Sales.status_code_id = Status_Codes.status_code_id;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT customer_id, CONCAT(Customers.first_name,' ', Customers.last_name) as customer_full_name FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        customers = cur.fetchall()

        query3 = "SELECT status_code_id, status FROM Status_Codes;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        status_codes = cur.fetchall()

        return render_template("Sales.j2", data=data, customers=customers, status_codes=status_codes)

        #### NEED IF STATEMENT FOR STATUS_CODE NULL VALUE ROUTING.

    if request.method == "POST":
        # Fires off if the user presses Add Sale Button
        if request.form.get("Add_Sale"):
            # grab customer form inputs
            sale_date = request.form["sale_date"]
            shipping_date = request.form["shipping_date"]
            customer_id = request.form["customer_id"]
            status_code_id = request.form["status_code_id"]

            # null value for status code
            if status_code_id == "":
                query = "INSERT INTO Sales (sale_date, shipping_date, customer_id) VALUES (%s, %s, %s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (sale_date, shipping_date, customer_id))
                mysql.connection.commit()      
            else:
                # no null inputs allowed
                query = "INSERT INTO Sales (sale_date, shipping_date, customer_id, status_code_id) VALUES (%s, %s, %s, %s);"
                cur = mysql.connection.cursor()
                cur.execute(query, (sale_date, shipping_date, customer_id, status_code_id))
                mysql.connection.commit()      

            # redirect back to sales page
            return redirect("/Sales")


# route for update functionality, updating the attributes of a sale in Sales

@app.route("/Update_Sale/<int:sale_id>", methods=["POST", "GET"])
def update_sale(sale_id):
    if request.method == "GET":
        
        query = "SELECT sale_id, sale_date, shipping_date, Customers.customer_id, Status_Codes.status_code_id, CONCAT(Customers.first_name,' ', Customers.last_name) as customer_full_name, Status_Codes.status as status FROM Sales INNER JOIN Customers ON Sales.customer_id = Customers.customer_id LEFT JOIN Status_Codes ON Sales.status_code_id = Status_Codes.status_code_id WHERE sale_id = %s;" % (sale_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT customer_id, CONCAT(Customers.first_name,' ', Customers.last_name) as customer_full_name FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        customers = cur.fetchall()

        query3 = "SELECT status_code_id, status FROM Status_Codes;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        status_codes = cur.fetchall()

        return render_template("Update_Sale.j2", data=data, customers=customers, status_codes=status_codes)

    if request.method == "POST":
        # fire off if user clicks the 'Edit Sale' button
        if request.form.get("Update_Sale"):
            # grab user form inputs
            sale_id = request.form["sale_id"]
            sale_date = request.form["sale_date"]
            shipping_date = request.form["shipping_date"]
            customer_id = request.form["customer_id"]
            status_code_id = request.form["status_code_id"]

            if status_code_id == "":
                query = "Update Sales SET sale_date = %s, shipping_date = %s, customer_id = %s, status_code_id = NULL WHERE sale_id = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (sale_date, shipping_date, customer_id, sale_id))
                mysql.connection.commit()
            else:
                query = "Update Sales SET sale_date = %s, shipping_date = %s, customer_id = %s, status_code_id = %s WHERE sale_id = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query, (sale_date, shipping_date, customer_id, status_code_id, sale_id))
                mysql.connection.commit()

            # redirect back to Sales page after we execute the update query
            return redirect("/Sales")

# ---------------------------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------------------------#
# Status Codes Page Routes
@app.route('/Status_Codes', methods=["POST", "GET"])
def Status_Codes_page():

    if request.method == "GET":
        # SQL query to grab all status codes in Status_Codes Database
        query = "Select * from Status_Codes;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template("Status_Codes.j2", data=data)


    if request.method == "POST":
        # Fires off if the user presses Add Status Code Button
        if request.form.get("Add_Status_Code"):
            # grab status code form inputs
            status = request.form["status"]

            # no null inputs allowed
            query = "INSERT INTO Status_Codes (status) VALUES (%s);"
            cur = mysql.connection.cursor()
            cur.execute(query, ([status]))
            mysql.connection.commit()      

            # redirect back to products page
            return redirect("/Status_Codes")


# ---------------------------------------------------------------------------------------------------------------------------------------#
# Purchase Orders to Products Page Routes 
@app.route('/Purchase_Orders_Products', methods=["POST", "GET"])
def Purchase_Orders_Products_page():

    if request.method == "GET":
        
        query = "SELECT purchase_order_product_id, Purchase_Orders.purchase_date, Products.name as product_name, purchase_quantity, purchase_price From Purchase_Orders_Products INNER JOIN Purchase_Orders ON Purchase_Orders.purchase_order_id = Purchase_Orders_Products.purchase_order_id INNER JOIN Products ON Products.product_id = Purchase_Orders_Products.product_id;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT purchase_order_id, purchase_date FROM Purchase_Orders;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        purchase_orders = cur.fetchall()

        query3 = "SELECT product_id, name FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        products = cur.fetchall()

        return render_template("Purchase_Orders_Products.j2", data=data, purchase_orders=purchase_orders, products=products)

    if request.method == "POST":

        if request.form.get("Add_Purchase_Order_Product"):

            purchase_order_id = request.form["purchase_order_id"]
            product_id = request.form["product_id"]
            purchase_quantity = request.form["purchase_quantity"]
            purchase_price = request.form["purchase_price"]

            # no null inputs allowed
            query = "INSERT INTO Purchase_Orders_Products (purchase_order_id, product_id, purchase_quantity, purchase_price) VALUES (%s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (purchase_order_id, product_id, purchase_quantity, purchase_price))
            mysql.connection.commit()      

            # redirect back
            return redirect("/Purchase_Orders_Products")


# route for update functionality, updating the attributes of a sale in Sales

@app.route("/Update_Purchase_Order_Product/<int:purchase_order_product_id>", methods=["POST", "GET"])
def update_purchase_order_product(purchase_order_product_id):
    if request.method == "GET":
        
        query = "SELECT purchase_order_product_id, Purchase_Orders.purchase_order_id as purchase_order_id, Products.product_id as product_id, Purchase_Orders.purchase_date, Products.name as product_name, purchase_quantity, purchase_price From Purchase_Orders_Products INNER JOIN Purchase_Orders ON Purchase_Orders.purchase_order_id = Purchase_Orders_Products.purchase_order_id INNER JOIN Products ON Products.product_id = Purchase_Orders_Products.product_id WHERE purchase_order_product_id = %s;" % (purchase_order_product_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT purchase_order_id, purchase_date FROM Purchase_Orders;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        purchase_orders = cur.fetchall()

        query3 = "SELECT product_id, name FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        products = cur.fetchall()

        return render_template("Update_Purchase_Order_Product.j2", data=data, purchase_orders=purchase_orders, products=products)

    if request.method == "POST":

        if request.form.get("Update_Purchase_Order_Product"):
            # grab user form inputs
            purchase_order_product_id = request.form["purchase_order_product_id"]
            purchase_order_id = request.form["purchase_order_id"]
            product_id = request.form["product_id"]
            purchase_quantity = request.form["purchase_quantity"]
            purchase_price = request.form["purchase_price"]

            query = "Update Purchase_Orders_Products SET purchase_order_id = %s, product_id = %s, purchase_quantity = %s, purchase_price = %s WHERE purchase_order_product_id = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (purchase_order_id, product_id, purchase_quantity, purchase_price, purchase_order_product_id))
            mysql.connection.commit()

            # redirect back
            return redirect("/Purchase_Orders_Products")

# route for delete functionality, deleting a purchase order from Purchase Orders,
@app.route("/Delete_Purchase_Order_Product/<int:purchase_order_product_id>")
def delete_purchase_order_product(purchase_order_product_id):
    # mySQL query to delete the customer with our passed id
    query = "DELETE FROM Purchase_Orders_Products WHERE purchase_order_product_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (purchase_order_product_id,))
    mysql.connection.commit()

    return redirect("/Purchase_Orders_Products")


# ---------------------------------------------------------------------------------------------------------------------------------------#
# Products to Sales routes
@app.route('/Products_Sales', methods=["POST", "GET"])
def Products_Sales_page():

    if request.method == "GET":
        
        query = "SELECT product_sale_id, Products.name as product_name, Sales.sale_date as sale_date, quantity_sold, unit_selling_price, total_price FROM Products_Sales INNER JOIN Products ON Products_Sales.product_id = Products.product_id INNER JOIN Sales ON Products_Sales.sale_id = Sales.sale_id;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT product_id, name FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        products = cur.fetchall()

        query3 = "SELECT sale_id, sale_date FROM Sales;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        sales = cur.fetchall()

        return render_template("Products_Sales.j2", data=data, products=products, sales=sales)

    if request.method == "POST":

        if request.form.get("Add_Product_Sale"):

            product_id = request.form["product_id"]
            sale_id = request.form["sale_id"]
            quantity_sold = request.form["quantity_sold"]
            unit_selling_price = request.form["unit_selling_price"]
            total_price = request.form["total_price"]

            # no null inputs allowed
            query = "INSERT INTO Products_Sales (product_id, sale_id, quantity_sold, unit_selling_price, total_price) VALUES (%s, %s, %s, %s, %s);"
            cur = mysql.connection.cursor()
            cur.execute(query, (product_id, sale_id, quantity_sold, unit_selling_price, total_price))
            mysql.connection.commit()      

            # redirect back
            return redirect("/Products_Sales")


# route for update functionality, updating the attributes of a sale in Sales

@app.route("/Update_Product_Sale/<int:product_sale_id>", methods=["POST", "GET"])
def update_product_sale(product_sale_id):
    if request.method == "GET":
        
        query = "SELECT product_sale_id, Products.product_id as product_id, Sales.sale_id as sale_id, Products.name as product_name, Sales.sale_date as sale_date, quantity_sold, unit_selling_price, total_price FROM Products_Sales INNER JOIN Products ON Products_Sales.product_id = Products.product_id INNER JOIN Sales ON Products_Sales.sale_id = Sales.sale_id WHERE product_sale_id = %s;" % (product_sale_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT product_id, name FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        products = cur.fetchall()

        query3 = "SELECT sale_id, sale_date FROM Sales;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        sales = cur.fetchall()

        return render_template("Update_Product_Sale.j2", data=data, products=products, sales=sales)

    if request.method == "POST":

        if request.form.get("Update_Product_Sale"):
            # grab user form inputs
            product_sale_id = request.form["product_sale_id"]
            product_id = request.form["product_id"]
            sale_id = request.form["sale_id"]
            quantity_sold = request.form["quantity_sold"]
            unit_selling_price = request.form["unit_selling_price"]
            total_price = request.form["total_price"]

            query = "Update Products_Sales SET product_id = %s, sale_id = %s, quantity_sold = %s, unit_selling_price = %s, total_price = %s WHERE product_sale_id = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (product_id, sale_id, quantity_sold, unit_selling_price, total_price, product_sale_id))
            mysql.connection.commit()

            # redirect back
            return redirect("/Products_Sales")

@app.route("/Delete_Product_Sale/<int:product_sale_id>")
def delete_product_sale(product_sale_id):

    query = "DELETE FROM Products_Sales WHERE product_sale_id = '%s'"
    cur = mysql.connection.cursor()
    cur.execute(query, (product_sale_id,))
    mysql.connection.commit()

    return redirect("/Products_Sales")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 19967))
    app.run(port=port, debug=True)