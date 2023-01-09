from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,check_password_hash




app= Flask(__name__)


app.secret_key="secretkey"


app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

source = PyMongo(app)


@app.route('/institute',methods =['POST'])
def nodal():
    _json =request.json
    nodal_officer=_json['nodal']
    Academic_year =_json['Academic_year']
    User_id =_json['user']
    password =_json['pwd']
    
    
     
    if nodal_officer and Academic_year and User_id and password and  request.method =='POST':
        _hashed_password = generate_password_hash(password)
        
        id = source.db.Institude_login.insert_one({'nodal':nodal_officer,'Academic_year':Academic_year, 'user':User_id ,'pwd':_hashed_password })
        
        resp = jsonify("User add  the institude login successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    





@app.route('/int_get_data')
def i1():
        Int1 = source.db.Institude_login.find()
        resp =dumps(Int1)
        return resp



@app.route("/kyc_one_data/<id>")
def i2():
    user = source.db.Institude_login.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    source.db.Institude_login.delete_one({'_id':ObjectId(id)})
    resp =jsonify("user deleted successfully")

    resp.status_code = 200

    return resp




@app.errorhandler(404)
def not_found(error =None):
    message ={
        'status':404,
        'message':"not found" + request.url
        
    }
    resp =jsonify(message)
    
    resp.status_code=404
    
    return resp




    
    

if __name__=="__main__":
    app.run(host='0.0.0.0')           
    
    
    







