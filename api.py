from fastapi import FastAPI
from models import CourseUpload,SignUp,Login,BillCalculation,UserEdit,CourseControl

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/CourseUpload/")
async def CoUp(coit : CourseUpload):
    return{"message" : "Test test"}

@app.post("/SignUp/")
async def SignUpFunc(sign : SignUp):
    return{"echo" : sign} 
    
@app.post("/Login/")
async def LoginFunc(logi : Login):
    return{"message" : "Test test"}

@app.post("/BillCalculation/")
async def BillCal(calcution : BillCalculation):
    return{"message" : "Test test"}

@app.post("/UserEdit/")
async def UserEd(usit : UserEdit):
    return{"message" : "Test test"}

@app.post("/CourseControl/")
async def CoCon(control : CourseControl):
    return{"message" : "Test test"}

