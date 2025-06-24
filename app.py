from flask import Flask, request, jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print("Received:", data)
    return jsonify({"message": "Data received"}), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050,debug=False)
