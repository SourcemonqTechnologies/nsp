from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request





app= Flask(__name__)


app.secret_key="secretkey"


app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp2"

source = PyMongo(app)

# institute profile update from
@app.route('/profile_update',methods =['POST', 'GET'])
def update():
    _json =request.json
    code=_json['n1']
    name_of_institute =_json['n2']
    code_directory=_json['n3']
    institute_nature =_json['n4']
    board_state =_json['n5']
    board_university =_json['n6']
    institute_address =_json['n7']
    institute_state =_json['n8']
    institute_district_direc =_json['n9']
    institute_district_code =_json['n10']
    institute_taluk_block=_json['n11']
    institute_tin=_json['n12']
    registration_certification =_json['n13']
    # contact person details
    aadhar_number =_json['n14']
    date_of_brith=_json['n15']
    moblie=_json['n16']
    email=_json['n17']
    # head of institution details
    name_of_aadhar=_json['n18']
    other_contact_num=_json['n19']
    designation=_json['n20']
    # bank deatils
    ifsc_code=_json['n21']
    ac=_json['n22']


    
    if code and name_of_institute  and code_directory and institute_nature and board_university and board_state and board_university and institute_address and institute_state and  institute_district_direc  and institute_district_code and institute_taluk_block and institute_tin and registration_certification  and aadhar_number and date_of_brith and moblie and name_of_aadhar and other_contact_num and designation and ifsc_code and ac   and request.method =='POST':
    
        
        id = source.db.institute_profile_update.insert_one({  
                                'n1'  : code,
                                'n2'  :  name_of_institute ,
                                'n3'  : code_directory ,
                                'n4'  : institute_nature,
                                'n5'  :   board_state ,
                                'n6'  : board_university,
                                'n7'  :institute_address,
                                'n8'  : institute_state, 
                                'n9'  : institute_district_direc, 
                                'n10' : institute_district_code ,
                                'n11' : institute_taluk_block ,
                                'n12' : institute_tin,
                                'n13' : registration_certification ,
                                'n14' : aadhar_number,
                                'n15' : date_of_brith ,
                                'n16' : moblie  ,
                                'n17' :email, 
                                'n18' : name_of_aadhar, 
                                'n19' :other_contact_num ,
                                'n20' : designation,
                                'n21' : ifsc_code, 
                                'n22' :ac 
                        
                                          })        
        resp = jsonify("User add  the institude login successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()


@app.route('/get')
def Iu1():
        In1 = source.db.institute_profile_update.find()
        resp =dumps(In1)
        return resp



@app.route("/user_one_data/<id>")
def Iu2():
    user = source.db.institute_profile_update.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    source.db.institute_profile_update.delete_one({'_id':ObjectId(id)})
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