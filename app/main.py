from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal,engine

from sqlalchemy.orm import Session

from .schema import EmployeeSchema

from .crud import get_employee,update_employee,create_employee,delete_employee,get_employee_by_id

from .models import EmployeeModel, Base

#
Base.metadata.create_all(bind=engine)


app=FastAPI()


def db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

@app.post('/create_employee/')

def create_employee_(employee:EmployeeSchema, db=Depends(db)):
    object_in_db=create_employee(db,employee)
   
    
    return True


@app.get('/consult_employee_by_id/')

def consult(db=Depends(db), employee_id:int = None):


    response=get_employee_by_id(db,employee_id)
    return f"The name of That employee is {response.employee_name}"




@app.get('/consult_employee_by_all/')

def consult(db=Depends(db)):


    response=get_employee(db)
    return response

@app.put("/update/employe/{employee_id}")
def update_employee_(employee_id:int,employee_salary:int,employee_position:str,employee_name:str,db=Depends(db) ):
    update_employee_(session=db,employee_id=employee_id, employee_salary=employee_salary,employee_position=employee_position,employee_name=employee_name)
    return "update done"
    


@app.patch("/update/emplyee_part/{employee_id}")

def update_employee_part(employee_id:int, employee:EmployeeSchema,db=Depends(db)):
    employee_data = employee.dict(exclude_unset=True)
    print(employee_data)
    response=update_employee(db, employee_data,employee_id)
    return response





@app.delete("/delete/employee/")
def delete( employee_id:int,db=Depends(db)):

    response=delete_employee(db,employee_id)
    return f"employee delete with success {response}"



