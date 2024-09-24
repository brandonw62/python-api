from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    # Example request: http://127.0.0.1:5000/get-user/123?extra="World"

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    if request.method == "POST":
        pass
    data = request.get_json()

    # Cant currently test in the browser. Tested with Postman

    return jsonify(data), 201
 
if __name__ == "__main__":
    app.run(debug=True)
