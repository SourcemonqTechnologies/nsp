from flask import Flask

from waitress import serve

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId               

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,check_password_hash





app= Flask(__name__)


app.secret_key ="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp2"


source = PyMongo(app)
monq =PyMongo(app)


# 1 fresh registration
@app.route('/fresh',methods =['POST',"GET"])
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
         
         
         
#2 login of institude 
@app.route('/institute',methods =['POST','GET'])
def nodal():
    _json =request.json
    nodal_officer=_json['nodal']
    Academic_year =_json['Academic_year']
    User_id =_json['user']
    password =_json['pwd']
    
    
     
    if nodal_officer and Academic_year and User_id and password and  request.method =='POST':
        _hashed_password = generate_password_hash(password)
        
        id = source.db.Institude_login.insert_one({'nodal':nodal_officer,'Academic_year':Academic_year, 'user':User_id ,'pwd':_hashed_password })
        
        resp = jsonify("User add  the institude login successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    
# 3 login of district

@app.route('/district',methods =['POST','GET'])
def district():
    _json =request.json
    _state =_json['state']
    _District = _json['district']
    


    if  _state and _District and  request.method =='POST':
        
        
        
        id= source.db.District_login.insert_one({'state':_state,
                    'district':_District})
        
        
        
        
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
      
    
    
    
 
  
#  4  student login 
@app.route('/loginF',methods =['POST','GET'])
def loginF():
    _json =request.json
    _application_id =_json['A_id']
    _password = _json['pwd']
    


    if  _application_id and _password and  request.method =='POST':
        _hashed_password = generate_password_hash(_password)
        
        
        id= source.db.login_fresh.insert_one({'A_id':_application_id,
                                                    'pwd':_hashed_password})
        resp = jsonify(" User is login successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
       
 
 
 
 
 
# 5 add request for institute head
 
@app.route('/request_form_ins',methods =['POST','GET'])
def khuhiun():
    _json =request.json
    institution =_json['f1']
    state =_json['f2']
    District = _json['f3']
    name =_json['f4']


    if  institution and state and District and name  and  request.method =='POST':
        
        
        
        id= source.db.request_form_for_adding_institute.insert_one({'f1':institution,
                                               'f2':state,
                                                'f3':District,
                                                'f4':name    })
          
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
      
    
 
 
#6 institude head aadhaar authentication
@app.route('/update',methods =['POST', 'GET'])
def dkjf():
    _json =request.json
    aadhar_number=_json['a1']
    name_of_aadhar =_json['a2']
    date_of_brith =_json['a3']
    gender =_json['a4']
    moblie =_json['a5']

    
    if aadhar_number and name_of_aadhar and date_of_brith and gender and moblie and request.method =='POST':
    
        
        id = source.db.institude_head_aadhaar_authentication .insert_one({
                        'a1':aadhar_number,
                        'a2':name_of_aadhar,
                        'a3':date_of_brith,
                        'a4':gender,
                        'a5':moblie
                                                    })        
        resp = jsonify("User  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()


# 7 validate your AISHE/DISE/NCVT code
@app.route('/kyc',methods =['POST','GET'])
def kadk():
    _json =request.json
    _code =_json['code']
    
    if  _code and   request.method =='POST':
        
        
        id= source.db.kyc_login.insert_one({'code':_code})
   
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()

 
 
 
 
 

# 8 institute profile update from
@app.route('/profile_update',methods =['POST', 'GET'])
def idks():
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
    
        
        id =monq.db.institute_profile_update.insert_one({  
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

 
 
 
# 9 institution aishe code 
@app.route('/AISHE_instite',methods =['POST' , 'GET'])
def institi():
    _json =request.json
    _institute_type =_json['instiute_type']
    _state = _json['state']
    _district = _json['district']
    _university_type = _json['untype']

    if  _institute_type and _state and _district and _university_type and  request.method =='POST':
        
        
        id= monq.db.instite_aishe.insert_one({'instiute_type':_institute_type,
                                            'state':_state,
                                           'district' :_district,
                                           "untype" : _university_type})
   
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
 
 
 
# 10 update institude head details
@app.route('/head_instite',methods =['POST' , 'GET'])
def mdhgd():
    _json =request.json
    aadhar_number =_json['a1']
    name_as_in_aaadhar = _json['a2']
    data_of_brith = _json['a3']
    gender = _json['a4']
    moblie_number=_json['a5']

    if  aadhar_number and name_as_in_aaadhar and data_of_brith and gender and moblie_number and request.method =='POST':
        
        
        id= source.db.update_institute_head_details.insert_one({'a1':aadhar_number,
                                            'a2':name_as_in_aaadhar,
                                           'a3' :data_of_brith,
                                           'a4' : gender,
                                           'a5':moblie_number})
   
        resp = jsonify(" submit  successfully")
        
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
    serve(app.run(host='0.0.0.0' ,port='2000' ,debug=True, ssl_context ="adhoc"))



