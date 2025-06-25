from flask import Flask, render_template
import os

# Tell Flask where to find templates and static files
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def home():
    try:
        print("Current dir:", os.getcwd())
        print("Templates content:", os.listdir('./templates'))
    except Exception as e:
        print("Error:", e)
    return render_template('index.html')


# Optional: add a health check
@app.route('/health')
def health():
    return 'OK', 200

# Needed for Vercel handler
def handler(environ, start_response):
    return app(environ, start_response)
