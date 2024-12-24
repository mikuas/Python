from flask import Flask, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret-key'

jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    # username = request.form.get('username')
    # username = request.json.get('username', None)
    password = request.form['password']

    if username != 'admin' or password != '114514':
        return {'message': 'Bad username or password'}, 401

    # identity is a simple string, like a username
    access_token = create_access_token(identity=username)
    return {'access_token': access_token}, 200

@app.route('/download', methods=['GET'])
def download():
    token = request.args.get('token')
    if token != 'this_is_ture_token':
        return 'token Error', 401
    else:
        return 'download file', 200

@app.route('/api', methods=['GET'])
@jwt_required
def api():
    current_user = get_jwt_identity()
    return "Hello, " + current_user

if __name__ == '__main__':
    app.run(debug=True)
