from sqlalchemy.orm import Session

from .schema import EmployeeSchema
from .models import EmployeeModel


# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
from fastapi import HTTPException
def create_employee(session:Session, employee:EmployeeSchema):

    insert_employee=EmployeeModel(**employee.dict())
    session.add(insert_employee)
    session.commit()
    session.refresh(insert_employee)
    return insert_employee

def get_employee_by_id(session:Session, employee_id:int):

    if employee_id is None:
        
        raise HTTPException(status_code=404, detail="employee id not None")
    else:
        return session.query(EmployeeModel).filter(EmployeeModel.employee_id==employee_id).first()

    

def get_employee(session:Session):

   
   
    return session.query(EmployeeModel).all()




def update_employee(session:Session,employee_id:int, employee_salary:int,employee_position:str,employee_name:str ):

    #get the emplyee id 

    response=get_employee_by_id(session, employee_id)
    #change

    if response:
        response.employee_name=employee_name
        response.employee_position=employee_position
        response.employee_salary=employee_salary
        session.commit()
        session.refresh(response)

        return response
    else:

        raise HTTPException(status_code=404,detail="employee id invailable ")
def update_employee_(session:Session, employee:dict,employee_id:int):
    response=get_employee_by_id(session,employee_id)
    if response is None:
        raise HTTPException(status_code=404, detail="employee not found")
    
    
    for key, value in employee.items():
         if key in ['employee_name', 'employee_position', 'employee_salary'] and value is not None:
            setattr(response,  key, value)
    
    session.commit()
    session.refresh(response)
    
    return response


def delete_employee(session:Session,employee_id:int):

    found_employee=session.query(EmployeeModel).filter(EmployeeModel.employee_id==employee_id).first()
    session.delete(found_employee)
    session.commit() 
    return "Employee delete"