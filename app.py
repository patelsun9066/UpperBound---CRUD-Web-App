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
        query = "SELECT purchase_order_id, purchase_date, delivery_date, vendor_id from Purchase_Orders WHERE purchase_order_id = %s;" % (purchase_order_id)
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

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 19967))
    app.run(port=port, debug=True)