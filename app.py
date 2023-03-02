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

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 19967))
    app.run(port=port, debug=True)