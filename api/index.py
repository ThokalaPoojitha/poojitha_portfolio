from flask import Flask, render_template
import os
# Get absolute paths relative to this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def home():
    return render_template('index.html')  # or 'index.html' if you want

if __name__ == '__main__':
    app.run(debug=True)
