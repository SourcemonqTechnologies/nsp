
from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request






app= Flask(__name__)

app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

monq = PyMongo(app)



# after the login screen the updateing the aadhar update 

@app.route('/update_aadhar',methods =['POST','GET'])
def district():
    _json =request.json
    _name_of_aadhar =_json['a1']
    aadhar_number =_json['a2']
    gender =_json['a3']
    alternate_contact =_json['a4']
    fax_number =_json['a5']
    pin =_json['a6']
    designation =_json['a7']
    communication =_json['a8']
    address =_json['a9']
    moblie_number =_json['a10']
    data_of_brith =_json['a11']
    telephone =_json['a12']
    moblie =_json['a13']
    email =_json['a14']
    office_address =_json['a15']
    permanent_address =_json['a16']
    
    
   
    if  _name_of_aadhar and aadhar_number and gender and alternate_contact and fax_number and pin and  email and  designation and communication and    address and moblie_number and data_of_brith and telephone and moblie and office_address and permanent_address    and   request.method =='POST':
        
        
        id= monq.db.after_aadhar_update.insert_one({'a1':_name_of_aadhar,
                                          'a2':aadhar_number,
                                                  'a3':gender,
                                                   'a4':alternate_contact,
                                                       'a5':fax_number,
                                                              'a6':pin,
                                                               'a7':designation,
                                                               'a8':communication,
                                                               'a9':address,
                                                          'a10':moblie_number,
                                                   'a11':data_of_brith,
                                                  'a12':telephone,
                                                 'a13':moblie,
                                                'a14':email,
                                             'a15':office_address,
                                              'a16':permanent_address})
   
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()



@app.route('/updat_get_data')
def kfuuf():
        d1 = monq.db.after_aadhar_update.find()
        resp =dumps(d1)
        return resp



@app.route("/uy_one_data/<id>")
def kkgj():
    user = monq.db.after_aadhar_update.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    monq.db.after_aadhar_update.delete_one({'_id':ObjectId(id)})
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