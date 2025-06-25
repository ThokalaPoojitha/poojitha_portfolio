from flask import Flask, render_template

# Must match the relative path of your templates
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    print("hello")
    return render_template('index.html')

# Required for Vercel serverless handler
def handler(environ, start_response):
    print("hey")
    return app.wsgi_app(environ, start_response)
