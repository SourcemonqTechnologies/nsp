from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request




app= Flask(__name__)




app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp2"

monq = PyMongo(app)



#  eligibility criteria
@app.route('/scheme_type',methods =['POST' , 'GET'])
def scheme():
    _json =request.json
    _domacile_state =_json['dsts']
    _course_level= _json['level']
    _religion = _json['religion']
    _caste = _json['cast']
    community = _json['community']
    gender = _json['gender']
    parent_annual =_json['parent']
    income = _json['income']

    if  _domacile_state   and _course_level  and _religion and _caste   and community and gender and parent_annual and income and request.method =='POST':
        
        
        id= monq.db.eligibility_criteria.insert_one({'dsts':_domacile_state,
                                            'level':_course_level,
                                           'religion' :_religion,
                                           "cast" : _caste,
                                           'community':community,
                                              'gender':gender,
                                              'parent':parent_annual,
                                              'income':income         })
   
    
   
   
  
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()






@app.route('/elig_get_data')
def elig1():
        ad1 = monq.db.eligibility_criteria.find()
        resp =dumps(ad1)
        return resp



@app.route("/elig_one_data/<id>")
def elig2():
    user1 = monq.db.eligibility_criteria.find({'_id':ObjectId(id)})
    resp = dumps(user1)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def dele(id):
    monq.db.eligibility_criteria.delete_one({'_id':ObjectId(id)})
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
