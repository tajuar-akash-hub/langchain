from langchain_groq import ChatGroq
from pydantic import BaseModel , EmailStr, Field
from typing import Optional 
from dotenv import load_dotenv

load_dotenv()

class JobApplication(BaseModel): 
    name : str = "Unknown"

    experience : Optional[int] = None

    email : EmailStr

    expected_salary : int = Field( gt =0  , description="Expected Annual Salary of the candidate" )


#create the model 

model = ChatGroq(model= "llama-3.3-70b-versatile")

#create a structured model 

structured_model = model.with_structured_output(JobApplication)


#invoke the model 

result = structured_model.invoke(
    """My name is Arif Hasan. I have 3 years of experience
    as a Machine Learning Engineer.

    My email is arif@gmail.com.
    I am expecting an annual salary of 50000 dollars.
    """
)

print(result)




