from flask import Flask
from flask import jsonify as json
from flask import abort, make_response, redirect, url_for, session, request
from flask_httpauth import HTTPBasicAuth
from werkzeug import secure_filename


auth = HTTPBasicAuth()
app = Flask(__name__)
app.secret_key = 'any random string'



#      username = session['username']
#       session['username'] = request.form['username']
#    session.pop('username', None)

#         abort(400)
#      return jsonify({'task': task}), 201


@auth.verify_password
def verify_password(username, password):
    if(username == 'roozbeh' and password == 'python') return True
    return False

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not ffoundd'},404))


@auth.error_handler
def unauthrized():
    return make_response(json({'error': "Unauthorized access"}), 403)


@app.route('/uploader', methods=['POST'])
def uploader_file():
    f = request.files['file']
    f.save(SAVE_FOLDER + secure_filename(f.filename))
    return "file successfully uploaded"


@app.route('/api/all', methods=['GET'])
@auth.login_required
def get():
    return jsonify({'tasks': "hala masaln hast dige"})


if (__name__ == '__main__'):
    app.run("0.0.0.0", 80, True)
