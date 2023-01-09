from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request




app= Flask(__name__)


app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

monq = PyMongo(app)


@app.route('/admi',methods =['POST'])
def admin():
    _json =request.json
    _course_level =_json['course_level']

    


    if  _course_level and  request.method =='POST':
        
        
        id= monq.db.administration.insert_one({'course_level':_course_level
                                                    })
   
   
   
   
  
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()





@app.route('/admi',methods =['POST'])
def adminksl():
    _json =request.json
    course =_json['course']
    course_year =_json['course_year']
    category =_json['category']
    gender =_json['gender']
    admin_fee =_json['admin_fee']
    tution_fee =_json['tution_fee']
    other_fee =_json['other_fee']


    if  course and course_year and category and gender and admin_fee and tution_fee and other_fee and  request.method =='POST':
        
        
        id= monq.db.administration.insert_one({'course':course,
                                               'course_year':course_year,
                                                'category': category,
                                                'gender':gender,
                                                'admin':admin_fee,
                                                'tution-fee':  tution_fee,
                                                'other_fee':other_fee})  
  
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()








@app.route('/adminn_dta')
def admiww():
        d1 = monq.db.administration.find()
        resp =dumps(d1)
        return resp



@app.route("/ad_one_data/<id>")
def ksdd():
    user = monq.db.administration.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    monq.db.administration.delete_one({'_id':ObjectId(id)})
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
