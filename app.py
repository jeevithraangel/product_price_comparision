from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "Product Service Running"}

@app.route("/products")
def products():
    return jsonify(["Laptop", "Phone", "Tablet"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)