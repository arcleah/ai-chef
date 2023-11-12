from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pantry.html')  # Assuming your HTML file is named 'index.html'

if __name__ == '__main__':
    app.run(debug=True)