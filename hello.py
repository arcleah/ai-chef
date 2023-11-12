from flask import Flask, request, render_template, redirect, url_for, session, flash
#from database import create_connection, login_user, create_user  # Importing the functions
import sqlite3
app = Flask(__name__)
app.secret_key = 'corn'  # for session management

database = r"C:\Users\yo-s-\Documents\GitHub\ai-chef\sqlite\database.db"  # Define the database path here

@app.route("/", methods = ['GET', "POST"])
def test():
    if request.method == 'POST':
        name = request.form.get('name')
        dietary_restrictions = request.form.get('dietary-restrictions')
        allergies = request.form.get('allergies')
        preferences = request.form.get('food-preferences')

        curr = sqlite3.connect(r"C:\Users\yo-s-\Documents\GitHub\ai-chef\sqlite\database.db")
        cursor = curr.cursor()

        query = "INSERT INTO users(name, dietary_restrictions, allergies, preferences) VALUES(?,?,?,?)"
        cursor.execute(query, (name, dietary_restrictions, allergies, preferences))

        results = cursor.fetchall()

        for i in results:
            print(i)

        curr.commit()

        cursor.close()
        curr.close()

        return "hello" + name + ""
    return render_template("mainpage.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    # error = None  # Define an error variable to hold the error message
    # if request.method == 'POST':
    #     email = request.form['email']
    #     password = request.form['password']
        
    #     conn = create_connection(database)
    #     auth_success = login_user(conn, email, password)
        
    #     if auth_success:
    #         session['logged_in'] = True
    #         session['user_id'] = email  # Or the actual user ID from the database
    #         return redirect(url_for('pantry'))
    #     else:
    #         error = "Invalid credentials"  # Set the error message
    
    # # If it's a GET request or credentials are wrong, show the login form again
    # return render_template("login.html", error=error)
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/pantry")
def pantry():
    return render_template("pantry.html")

if __name__ == "__main__":
    app.run()