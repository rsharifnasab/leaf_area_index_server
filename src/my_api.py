#!/usr/bin/env python
import os
from flask import Flask, abort, request, jsonify, url_for, abort, make_response
from flask_httpauth import HTTPBasicAuth
from db import DB
from area import leaf_area_calculate
# initialization
app = Flask(__name__)
app.secret_key = 'the quick brown fox jumps over the lazy dog'

# extensions
auth = HTTPBasicAuth()
db = DB("../","users.txt","tmp-files")


@auth.verify_password
def verify_password(token, client):
    if not db.verify_client(client): return False
    if not db.verify_auth_token(token): return False
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

@app.route('/api/calculate' , methods = ['POST'])
@auth.login_required
def calculator():
    username = "null"
    try:
        username = auth.username()
        project_name =  request.form.get("proj")
        save_path = db.save_attach( request.files['file'] , username , project_name)
        return jsonify({'area': '%s'%leaf_area_calculate(save_path)})
    except:
        abort(400)
    finally:
        db.clean_attach(username)

@app.route('/uploader', methods=['POST'])
def uploader_file():
    f = request.files['file']
    f.save(SAVE_FOLDER + secure_filename(f.filename))
    return "file successfully uploaded"

app.run(host = "0.0.0.0" , port = 80, debug = True)
