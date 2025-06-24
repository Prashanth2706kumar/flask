from flask import Flask, request, jsonify
from flask_cors import CORS
import os
app=Flask(__name__)
CORS(app)

port = int(os.environ.get("PORT", 5050)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print("Received:", data)
    return jsonify({"message": "Data received"}), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=port,debug=False)
