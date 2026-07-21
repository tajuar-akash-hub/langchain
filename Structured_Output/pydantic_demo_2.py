from pydantic import BaseModel , EmailStr, Field
from typing import Optional 

class JobApplication(BaseModel): 
    name : str = "Unknown"

    experience : Optional[int] = None

    email : EmailStr

    expected_salary : int = Field( gt =0 , description="Expected Annual Salary of the candidate" )



new_application = {
    "email": "abc@gmail.com", 
    "experience": "3", 
    "expected_salary" : 50000
}

application = JobApplication(**new_application)

# print(application)

#convert pydantic object to dictionary 

application_dict = application.model_dump()

# print(application_dict)

print(application_dict['experience'])


#convert pydantic object to json

application_json = application.model_dump_json()

print(application_json)