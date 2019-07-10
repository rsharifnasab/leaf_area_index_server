import os
from flask import Flask, abort, request, jsonify, url_for, abort, make_response, redirect
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

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error':'bad request'},404))


@auth.error_handler
def unauthrized():
    return make_response(jsonify({'error': "unauthorized access , please use valid username and password"}), 403)


@app.route('/api/help', methods = ['GET'])
def get_resource():
    return jsonify({'help': 'hello, this is how to use this api: you should send post message to : api/calculate and attah image file as (file) and project name as (proj), pls dont forgot that you need authenticate first with valid username and password'})

@app.route('/api/calculate' , methods = ['GET'])
def go_to_help():
    return redirect(url_for("get_resource"))

@app.route('/api/calculate' , methods = ['POST'])
@auth.login_required
def calculator():
    username = "null"
    try:
        username = auth.username()
        project_name =  request.form.get("proj")
        save_path = db.save_attach( request.files['file'] , username , project_name)
        return jsonify({'area': '%s'%leaf_area_calculate(save_path)}) #todo : also return the new image file
    except:
        abort(400)
    finally:
        db.clean_attach(username) #todo : if send multiple times

#if __name__ == '__main__':
#    app.run(host = "0.0.0.0" , port = 80, debug = True)
