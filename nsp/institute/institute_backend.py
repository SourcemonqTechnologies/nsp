from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request





app= Flask(__name__)


app.secret_key="secretkey"


app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

source = PyMongo(app)

# general information of intitude
@app.route('/int',methods =['POST', 'GET'])
def nodal():
    _json =request.json
    State_of_domicile=_json['state']
    scholarship_catrgory =_json['scholarship']
    ration_card_no =_json['ration']
    name_of_student =_json['name']
    ration_card_memberid =_json['member_id']
    Name_as_ration_card =_json['name_ration_card']
    annual_family_income =_json['annual_income']
    day_scholar_hosteler =_json['hosteler']
    mobile_number =_json['mobile']
    community_category =_json['community']
    aadhar=_json['aadhar']
    email=_json['email']
    gender =_json['gender']
    religion =_json['religion']





    
    if State_of_domicile and scholarship_catrgory and ration_card_no and name_of_student and ration_card_memberid and Name_as_ration_card and annual_family_income and day_scholar_hosteler and mobile_number and community_category and aadhar and email and gender and religion  and request.method =='POST':
    
        
        id = source.db.Institude_backend.insert_one({
                        'state':State_of_domicile,
                        'scholarship':scholarship_catrgory,
                        'ration':ration_card_no,
                        'name': name_of_student,
                        'member_id':ration_card_memberid,
                        'name_ration_card':Name_as_ration_card,
                        'annual_income':annual_family_income,
                        'hosteler':day_scholar_hosteler,
                        'mobile':mobile_number,
                        'community':community_category,
                        'aadhar':aadhar,
                        'email':email,
                        'gender':gender,
                        'religion':religion
                                          })        
        resp = jsonify("User add  the institude login successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()


@app.route('/get')
def I1():
        In1 = source.db.Institude_backend.find()
        resp =dumps(In1)
        return resp



@app.route("/user_one_data/<id>")
def I2():
    user = source.db.Institude_backend.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    source.db.Institude_backend.delete_one({'_id':ObjectId(id)})
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
    
    
    
