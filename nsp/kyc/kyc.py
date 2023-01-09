
from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request






app= Flask(__name__)

app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

monq = PyMongo(app)

# validate your AISHE/DISE/NCVT code
@app.route('/kyc',methods =['POST','GET'])
def district():
    _json =request.json
    _code =_json['code']
    
    if  _code and   request.method =='POST':
        
        
        id= monq.db.kyc_login.insert_one({'code':_code})
   
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()



@app.route('/kyc_get_data')
def d1():
        d1 = monq.db.kyc_login.find()
        resp =dumps(d1)
        return resp



@app.route("/kyc_one_data/<id>")
def d2():
    user = monq.db.kyc_login.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    monq.db.kyc_login.delete_one({'_id':ObjectId(id)})
    resp =jsonify("user deleted successfully")

    resp.status_code = 200

    return resp






@app.route('/update/<id>',methods =['PUT'])
def update(id):
    _id =id
    _json =request.json
    _code =_json['code']   
    


    if  _code and   request.method =='POST':
        
        
        id= monq.db.kyc_login.insert_one({'_id': ObjectId (_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                                                                {'$set':{'code':_code}})

        resp = jsonify("user updataed the data")

        resp.status_code =200

        return resp





# kyc for the Institude Nodal officer
        
@app.route('/kyc_inti',methods =['POST','GET'])
def kyc2():
    _json =request.json
    _Aadhar =_json['aadhar']
    _Name_of_aadhar =_json['name_aadhar']
    _date_of_birth =_json['birth']
    _gender =_json['gender']
    _moblie=_json['_moblie']


    if  _Aadhar and _Name_of_aadhar and _date_of_birth and _gender and _moblie and  request.method =='POST':
        
        
        id= monq.db.kyc_institude.insert_one({'aadhar':_Aadhar,'name_addhar':_Name_of_aadhar , 'birth':_date_of_birth,'gender':_gender ,'moblie':_moblie })
   
        resp = jsonify(" submited  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()




# kyc institude head details
@app.route('/kyc_inti2',methods =['POST','GET'])
def kyc3():
    _json =request.json
    _Aadhar =_json['aadhar']
    _Name_of_aadhar =_json['name_aadhar']
    _date_of_birth =_json['birth']
    _gender =_json['gender']
    _moblie=_json['_moblie']



    if  _Aadhar and _Name_of_aadhar and _date_of_birth and _gender and  request.method =='POST':
        
        
        id= monq.db.kyc_institude_head.insert_one({'aadhar':_Aadhar,'name_addhar':_Name_of_aadhar , 'birth':_date_of_birth,'gender':_gender,'moblie':_moblie })
   
        resp = jsonify(" submited  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()








# kyc of registration forms for institide 
@app.route('/kyc_inti3',methods =['POST','GET'])
def kyc4():
    _json =request.json
    _insitute_name =_json['a1']
    _insitute_address =_json['a2']
    _state =_json['a3']
    _district =_json['a4']
    _affillated_board =_json['a5']
    _institute_nature =_json['a6']
    _total_strength =_json['a7']
    _Url = _json['a8']
    _aadhar1 =_json['a9']
    _Name_of_aadhar2 =_json['a11']
    _date_of_birth3 =_json['a12']
    _gender4 =_json['a13']
    _email5 =_json['a14']
    _designation =_json['a15']    
    





    if  _insitute_name and _insitute_address and _state and _district and _district and _affillated_board and _institute_nature and _total_strength and _Url and  _aadhar1 and _Name_of_aadhar2 and _date_of_birth3 and _gender4 and _email5 and _designation  and request.method =='POST':
        
        
        id= monq.db.kyc_registration.insert_one({'a1':_insitute_name,
                                                'a2':_insitute_address ,
                                                 'a3':_state,
                                                 'a4':_district,
                                                 'a5':_affillated_board,
                                                 'a6':_institute_nature,
                                                 'a7':_total_strength,
                                                 'a8':_Url, 
                                                 'a9':_aadhar1,
                                                 'a11':_Name_of_aadhar2,
                                                 'a12':_date_of_birth3,
                                                 'a13':_gender4,
                                                 'a14':_email5,
                                                 'a15':_designation})
   
        resp = jsonify(" submited  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()





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