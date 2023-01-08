from main import *
from models import User, Newsletter, db

@app.route("/api/v1")
def status():
	return jsonify({
		"message": "Online"
	})

@app.route('/api/v1/create/user', methods=["POST"])
def createUser():
	try:
		data = request.get_json()
		userData = {
			"username": data["username"],
			"password": data["password"],
			"email": data["email"],
			"telephone": data["telephone"] or ""
		}
		user = User("banco.db")
		user.createUser(userData["username"], userData["password"], userData["email"], userData["telephone"])

		return jsonify({
			"message": "OK"
		})
	except Exception as e:
		return jsonify({
			"message": e
		})

@app.route("/api/v1/login", methods=["GET"])
def loginUser():
	username = request.args.get('username')
	senha = request.args.get("password")
	user = User("banco.db")
	if user.authUser(username, senha) == "User Not Exists":
		return jsonify({
			"message": "User Not Exists"
			})

	else:
		return jsonify({
			"message": "success"
			})


	
