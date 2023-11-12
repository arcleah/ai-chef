from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
import sqlite3
from openai import OpenAI
import json

app = Flask(__name__)
app.secret_key = 'corn'  # for session management
correct_email = 'johndoe123@gmail.com'
correct_password = '1234'
client = OpenAI(api_key="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")

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
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == correct_email and password == correct_password:
            # Correct credentials, redirect to pantry page
            return redirect(url_for('pantry'))
        else:
            # Incorrect credentials
            flash('Invalid username or password', 'error')
            return render_template("login.html",)

    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/pantry")
def pantry():
    return render_template("pantry.html")

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    items = data['itemsData']
    
    # Construct the prompt with items details
    prompt = "Here are the items in the pantry:\n"
    for item in items:
        prompt += f"Produce: {item['produce']}, Quantity: {item['quantity']}, Expiry Date: {item['expiryDate']}\n"
    prompt += "Generate a recipe using these ingredients."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    # Extract the recipe content from the response
    recipe_content = response.choices[0].message.content

    # Return the recipe content in JSON format
    return jsonify({'recipe': recipe_content})


if __name__ == "__main__":
    app.run()