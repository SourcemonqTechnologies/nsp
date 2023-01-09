from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request





app= Flask(__name__)





app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

mongo = PyMongo(app)

# search of the institite
@app.route('/search',methods =['POST', 'GET'])
def nodal():
    _json =request.json
    insitution_state=_json['state']
    insitution_collage =_json['collage']
    insitution_district =_json['district']
    school_collage_iti =_json['or']

    
    if insitution_state and insitution_collage and insitution_district and school_collage_iti  and request.method =='POST':
    
        
        id = mongo.db.search_of_institute.insert_one({
                        'state':insitution_state,
                        'collage':insitution_collage,
                        'district':insitution_district,
                        'or':school_collage_iti
                                                    })        
        resp = jsonify("User  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()


@app.route('/get')
def sI1():
        sIn1 = mongo.db.search_of_institute.find()
        resp =dumps(sIn1)
        return resp



@app.route("/user_one_data/<id>")
def sI2():
    user = mongo.db.search_of_institute.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    mongo.db.search_of_institute.delete_one({'_id':ObjectId(id)})
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
    
    
    