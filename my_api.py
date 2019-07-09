#!/usr/bin/env python
import os
from flask import Flask, abort, request, jsonify, url_for, abort, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug import secure_filename
from db import DB

# initialization
app = Flask(__name__)
app.secret_key = 'the quick brown fox jumps over the lazy dog'

# extensions
auth = HTTPBasicAuth()
db = DB("users.txt")


@auth.verify_password
def verify_password(token, client):
    if not db.verify_client(client): return False
    print("client ok")
    if not db.verify_auth_token(token): return False
    print("username ok")
    return True

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'api not found'},404))


@auth.error_handler
def unauthrized():
    return make_response(jsonify({'error': "customized unauthorized access"}), 403)


@app.route('/api/resource', methods = ['GET'])
@auth.login_required
def get_resource():
    return jsonify({'data': 'everything is ok in get'})

@app.route('/api/resource' , methods = ['POST'])
@auth.login_required
def post_api():
    return jsonify({'data': 'everything is ok in post'})

@app.route('/uploader', methods=['POST'])
def uploader_file():
    f = request.files['file']
    f.save(SAVE_FOLDER + secure_filename(f.filename))
    return "file successfully uploaded"

app.run(host = "0.0.0.0" , port = 80, debug = True)
