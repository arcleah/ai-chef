from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def aboutus():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)