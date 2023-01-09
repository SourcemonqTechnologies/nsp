from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request





app= Flask(__name__)





app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp2"

mongo = PyMongo(app)

# update aadhar details of instiitute head
@app.route('/update',methods =['POST', 'GET'])
def nodal():
    _json =request.json
    aadhar_number=_json['a1']
    name_of_aadhar =_json['a2']
    date_of_brith =_json['a3']
    gender =_json['a4']
    moblie =_json['a5']

    
    if aadhar_number and name_of_aadhar and date_of_brith and gender and moblie and request.method =='POST':
    
        
        id = mongo.db.update_aadhaar_details_institute_head.insert_one({
                        'a1':aadhar_number,
                        'a2':name_of_aadhar,
                        'a3':date_of_brith,
                        'a4':gender,
                        'a5':moblie
                                                    })        
        resp = jsonify("User  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()


@app.route('/get')
def sI1():
        sIn1 = mongo.db.update_aadhaar_details_institute_head.find()
        resp =dumps(sIn1)
        return resp



@app.route("/user_one_data/<id>")
def sI2():
    user = mongo.db.update_aadhaar_details_institute_head.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    mongo.db.update_aadhaar_details_institute_heade.delete_one({'_id':ObjectId(id)})
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
    
    
    