from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render with Waitress!"

if __name__ == '__main__':
    # For local development
    app.run(host='0.0.0.0', port=5000)
else:
    # For production on Render
    serve(app, host='0.0.0.0', port=10000)

