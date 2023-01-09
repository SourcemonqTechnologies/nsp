from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request




app= Flask(__name__)




app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp2"

monq = PyMongo(app)


#___________________-_______ search scheme  wise nodal officer_________________________________-____________________





# state
@app.route('/search_scheme',methods =['POST' , 'GET'])
def offeri():
    _json =request.json
    _ministry =_json['ministry']
    _state= _json['state']
    _scheme = _json['schrme']
    

    if  _ministry   and _state and  _scheme and  request.method =='POST':
        
        
        id= monq.db.search_scheme_wise_nodal_office.insert_one({'ministry': _ministry,
                                            'state':_state,
                                           'schrme' :_scheme})
   
    
   
   
  
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()





# district
@app.route('/search_scheme_dis',methods =['POST' , 'GET'])
def juci():
    _json =request.json
    _ministry =_json['ministry']
    _state= _json['state']
    _scheme = _json['schrme']
    _district =_json['district']
    

    if  _ministry   and _state and  _scheme and _district and request.method =='POST':
        
        
        id= monq.db.search_scheme_wise_nodal_office.insert_one({'ministry': _ministry,
                                            'state':_state,
                                           'schrme' :_scheme,
                                           'district':_district    })
   
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()




# ministry
@app.route('/search_scheme_mini',methods =['POST' , 'GET'])
def kgofp():
    _json =request.json
    _ministry =_json['ministry']
    
    

    if  _ministry     and request.method =='POST':
        
        
        id= monq.db.search_scheme_wise_nodal_office.insert_one({'ministry': _ministry,
                                                                           })
   
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()

# zones
@app.route('/search_scheme_zone',methods =['POST' , 'GET'])
def sjdlz():
    _json =request.json
    _zone=_json['zone']
    
    

    if  _zone     and request.method =='POST':
        
        
        id= monq.db.search_scheme_wise_nodal_office.insert_one({'ministry': _zone,
                                                                           })
   
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()






@app.route('/scheme_get_data')
def schuy():
        ad1 = monq.db.search_scheme_wise_nodal_office.find()
        resp =dumps(ad1)
        return resp



@app.route("/elig_one_data/<id>")
def scgy():
    user1 = monq.db.search_scheme_wise_nodal_office.find({'_id':ObjectId(id)})
    resp = dumps(user1)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def dele(id):
    monq.db.search_scheme_wise_nodal_office.delete_one({'_id':ObjectId(id)})
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
