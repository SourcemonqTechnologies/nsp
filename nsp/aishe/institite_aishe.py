from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request
app= Flask(__name__)




app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp2"

monq = PyMongo(app)

#  institution aishe code
@app.route('/AISHE_instite',methods =['POST' , 'GET'])
def institi():
    _json =request.json
    _institute_type =_json['instiute_type']
    _state = _json['state']
    _district = _json['district']
    _university_type = _json['university_type']

    if  _institute_type and _state and _district and _university_type and  request.method =='POST':
        
        
        id= monq.db.instite_aishe.insert_one({'type':_institute_type,
                                            'district':_state,
                                           'district' :_district,
                                           "untype" : _university_type})
   
   
   
   
  
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()






@app.route('/AIS_get_data')
def AISin():
        ad1 = monq.db.instite_aishe.find()
        resp =dumps(ad1)
        return resp



@app.route("/AIS_one_data/<id>")
def AISin2():
    user1 = monq.db.instite_aishe.find({'_id':ObjectId(id)})
    resp = dumps(user1)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    monq.db.instite_aishe.delete_one({'_id':ObjectId(id)})
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
