from pydantic import BaseModel
from typing import Optional


class EmployeeSchema(BaseModel):

    employee_id:int
    employee_name:str
    employee_position:str
    employee_salary:float
    class Config:
        orm_mode=True