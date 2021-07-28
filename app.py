from flask import Flask, request, jsonify, redirect, url_for
import uuid
from user_app.user_operations import user
from flask_expects_json import expects_json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Ruba!"

create_scema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" },
    "address": { "type": "string" },
    "married_status": { "type": "string" },
    "DOB": { "type": "string" },
    "mobile": { "type": "string" },
  },
  "required": ["name", "age", "mobile", "address", "married_status", "DOB"]
}
@app.route('/users', methods=['POST', 'Get'])
@expects_json(create_scema, ignore_for=['GET'])
def user_func():
    if request.method == 'POST':
        data = request.json
        user1 = user()
        user_data = user1.create_user(data)
        # return redirect(f"users/{user_data}")
        return jsonify(user_data), 201
    else:
        user1 = user()
        users = user1.get_users()
        return jsonify(users)

@app.route('/users/<user_id>', methods=['GET', 'PATCH', 'DELETE'])
@expects_json(create_scema, ignore_for=['GET', 'DELETE'])
def user_func1(user_id):
    try:
        user_id = uuid.UUID(str(user_id), version=4)
        print(type(user_id))
        if request.method == 'GET':
            user1 = user()
            user2 = user1.get_user(str(user_id))

            if user2:
                return jsonify(user2)
            else:
                return 'Resource not found for {}'.format(user_id), 404  

        elif request.method == "PATCH":
            data = request.json
            user1 = user()
            user2 = user1.modify_user(str(user_id), data)
            if user2:
                return redirect(f"users/{str(user_id)}")
            else:
                return 'Resource not found for {}'.format(user_id), 404     

        elif request.method == "DELETE":
            user1 = user()
            user2 = user1.delete_user(str(user_id))
            if user2:
                return '', 204
            else:
                return 'Resource not found for {}'.format(user_id), 404
    except ValueError:
        return 'invalid UUID {}'.format(user_id), 400
    
# app.run(host='0.0.0.0', port=8080, debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)    