from .database import Base
from sqlalchemy import Column, String, Boolean,Float, Integer



class EmployeeModel(Base):
    __tablename__ ='EmployeeModel'
    employee_id=Column(Integer, primary_key=True, autoincrement=True)
    employee_name= Column(String)
    employee_position=Column(String)
    employee_salary=Column(Float)



