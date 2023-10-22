import csv

from flask_mysqldb import MySQL
from flask import Flask, render_template , request, redirect, url_for


app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '0.0.0.0'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'amazon'

mysql = MySQL(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! to Ecomm Amazon'

@app.route('/index') # default method is GET
def index():
    return render_template('index.html')


@app.route('/form', methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        return 'POST-method does not exist'
    else:
        return render_template('customer_form.html')

@app.route('/loginform', methods = ['POST', 'GET'])
def loginform():
    if request.method == 'POST':
        return 'POST-method does not exist'
    else:
        return render_template('login_form.html')

@app.route('/register_customer', methods = ['POST', 'GET'])
def register_customer():
    if request.method == 'GET':
        print("Im inside GET method")
        return 'GET-method does not exist'
    else:

        ## HTML Data
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = int(request.form['age'])
        print(f"Age = {age}")
        address = request.form['address']
        phone_number = int(request.form['phone_number'])
        credit_card = int(request.form['credit_card'])
        email_address = request.form['email_address']

        # Create Cursor
        cursor = mysql.connection.cursor()

        # Write Query and pass values from html
        cursor.execute('''
            INSERT INTO customers (username, password, first_name, last_name, age, address, phone_number, credit_card, email_address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (username, password, first_name, last_name, age, address, phone_number, credit_card, email_address))

        # commit changes after query execution
        mysql.connection.commit()
        # close the cursor
        cursor.close()
        return 'Customer data saved successfully.'

@app.route('/login_customer', methods = ['POST', 'GET'])
def login_customer():
    if request.method == 'GET':
        print("Im inside GET method")
        return 'GET-method does not exist'
    else:
        ## HTML Data
        username = request.form['username']
        password = request.form['password']

        # Create Cursor
        cursor = mysql.connection.cursor()

        # Write Query and pass values from html
        cursor.execute('''
            SELECT * FROM customers WHERE username = %s AND password = %s ;
            ''', (username, password))
        account = cursor.fetchone()
        # close the cursor
        cursor.close()
        if account:
            print("Display Products - Login successfully.")
            return render_template("upload_products.html")
        else:
            print("Login failed")
            return render_template("login_form.html")


@app.route('/uploadProducts', methods = ['POST', 'GET'])
def uploadProducts():
    if request.method == 'GET':
        print("Im inside GET method")
        return 'GET-method does not exist'
    else:
        if 'file' in request.files:
            csv_file = request.files['file']

            if csv_file.filename != '':
                # Check if the file is ending with .csv
                if csv_file.filename.endswith('.csv'):
                    # Read and insert data from the CSV file
                    cursor = mysql.connection.cursor()

                    # Read and insert data from the CSV file
                    csv_data = csv.reader(csv_file.stream.read().decode('utf-8').splitlines())
                    for row in csv_data:
                        product_id = row[0]
                        product_name = row[1]
                        category = row[2]
                        description = row[3]
                        price = float(row[4])
                        quantity = int(row[5])
                        freeshipping = bool(row[6])

                        cursor.execute('''INSERT into products(product_id, product_name, category, description, price,quantity,freeshiping)
                                              VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                                   (product_id, product_name, category,description ,price,quantity,freeshipping))

                    mysql.connection.commit()
                    cursor.close()
                    return redirect(url_for('display_products'))

    return 'Upload failed..!!'


@app.route('/display_products')
def display_products():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM amazon.products")
        products = cursor.fetchall()
        cursor.close()
        print(f"sample data display {products}")
        return render_template('products.html', products=products)
    except Exception as e:
        return str(e)

# Function to get products from the database
def get_products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM amazon.products")
    products = cursor.fetchall()
    cursor.close()
    return products

@app.route('/products')
def display_products_old():
    products = get_products()
    return render_template('upload_products.html', products=products)

@app.route('/analysis/product', methods=['GET'])
def statistical_analysis_products():
    conn = mysql.connection # Change to your database
    cursor = conn.cursor()

    # Analysis 1: Total Stock Quantity
    cursor.execute("select sum(quantity) From products;")
    total_stock_quantity = cursor.fetchone()[0]

    # Analysis 2: Average Price by Category
    cursor.execute("select category, AVG(PRICE) From products GROUP BY CATEGORY;")
    average_prices_by_category = cursor.fetchall()

    # Analysis 3: Most Expensive and Least Expensive Products
    cursor.execute("select product_name, price from  products where price =(select max(price) from products);")
    most_expensive_product = cursor.fetchone()
    cursor.execute("select product_name, price from  products where price =(select min(price) from products);")
    least_expensive_product = cursor.fetchone()

    # Analysis 4: Count of Products per Manufacturer
    cursor.execute("select Category, count(*) from products GROUP BY Category;")
    products_per_manufacturer = cursor.fetchall()

    # Analysis 5: Price Range Analysis
    cursor.execute("SELECT MIN(price), MAX(price) FROM products")
    price_range_data = cursor.fetchone()

    # Close the database connection
    cursor.close()

    return render_template('analysis.html',
                           total_stock_quantity=total_stock_quantity,
                           average_prices_by_category=average_prices_by_category,
                           most_expensive_product=most_expensive_product,
                           least_expensive_product=least_expensive_product,
                           products_per_manufacturer=products_per_manufacturer,
                           price_range_data=price_range_data)



if __name__ == '__main__':
    app.run()
