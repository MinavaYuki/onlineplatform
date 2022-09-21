from typing import Optional
from pydantic import BaseModel

class CourseUpload(BaseModel):
    course_video : str
    course_videoname : str
    description : str
    course_name : str
    course_price : int
    course_status : Optional[int] = 1

class SignUp(BaseModel):
    user_email: str
    user_password: str
    user_fname: str
    user_lname: str
    user_gender: int
    user_priority : Optional[int] = 1
    

class Login(BaseModel):
    user_email : str
    user_password : str
    #token : str

class BillCalculation(BaseModel):
    user_id : int
    course_id : int
    course_price : int

class UserEdit(BaseModel):
    user_fname: str
    user_lname: str
    user_gender: int

class CourseControl(BaseModel):
    course_status : int

'''class PurchaseHistory(BaseModel):
    user_bill : user_bill

class UserCourse(BaseModel):
    user_course : user_course
class user_course(BaseModel):
    course_id : int
    course_name : str
    course_videoname :str

class Register_log(BaseModel):
    user_id : int

class UserPurchaseHistory(BaseModel):
    user_id : int
    user_bill : user_bill

class user_bill(BaseModel):
    course_id : int
    bill_total : int'''

'''{"user_email":"mymail@gmail.com",
"user_password":"Mypass12",
"user_fname":"Fullname",
"user_lname":"Lastname",
"user_gender":"male",รับค่าเป็น 0 กับ 1 ควรใส่อะไรวะ
"user_phone":"0234562345"}

{"user_email":"mymail@gmail.com",
"user_password":"Mypass12"}

{"course_name":"คอร์ส Python",
"course_video":"link",
"course_videoname":"ชื่อคอร์ส",
"description": "คำอธิบายคอร์ส",
"course_price": 10000}

{"bill_total":  20000}'''