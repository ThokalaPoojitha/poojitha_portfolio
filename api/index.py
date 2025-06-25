from flask import Flask, render_template
import os

# Tell Flask where to find templates and static files
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    print("Current directory:", os.getcwd())
    print("Files here:", os.listdir('.'))
    print("Templates folder:", os.listdir('./templates') if os.path.exists('./templates') else 'templates not found')
    return render_template('index.html')


# Optional: add a health check
@app.route('/health')
def health():
    return 'OK', 200

# Needed for Vercel handler
def handler(environ, start_response):
    return app(environ, start_response)
