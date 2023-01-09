from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request




app= Flask(__name__)




app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

source = PyMongo(app)


@app.route('/fresh',methods =['POST','GET'])
def fresh():
    _json =request.json
    _state_of_Domicile =_json['domicile']
    _Name_of_student = _json['student']
    _Data_of_Birth = _json['birth']
    _mobile_number = _json['mobile']
    _bank_ifsc = _json['ifsc']
    _bank_A_c_no = _json['bank']
    _identification_details =_json['details']
    _scholorship_category =_json['category']
    _scheme_type = _json['scheme']
    _Gender = _json['gender']
    _Email_id =_json['email']


    
    if  _state_of_Domicile and _Name_of_student and _Data_of_Birth and _mobile_number and _bank_ifsc and _bank_A_c_no and _identification_details and _scholorship_category and _scheme_type and _Gender and _Email_id and  request.method =='POST':
        
        
        id= source.db.fresh_registration.insert_one({'domicile':_state_of_Domicile,
                                                      'student':_Name_of_student,
                                                      'birth':_Data_of_Birth,
                                                      'mobile':_mobile_number,
                                                       'ifsc':_bank_ifsc,
                                                       'bank':_bank_A_c_no,
                                                       'details':_identification_details,
                                                       'category':_scholorship_category,
                                                       'scheme':_scheme_type,
                                                       'gender':_Gender,
                                                       'email':_Email_id})
        
        resp = jsonify("User data add  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    

    



@app.route('/fresh_get_data')
def f1():
        f1 = source.db.fresh_registration.find()
        resp =dumps(f1)
        return resp



@app.route("/fresh_one_data/<id>")
def d2():
    user = source.db.fresh_registration.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    source.db.fresh_registration.delete_one({'_id':ObjectId(id)})
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



