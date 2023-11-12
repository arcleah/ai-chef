from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

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

        return "hello" + name + "!"
    return render_template("profile.html")

if __name__ == "__main__":
    app.run()

