from pydantic import BaseModel

class User(BaseModel): 
    name : str
    age : int

user_data = {
    "name" : "John",
    "age" : "25"
}

user = User(**user_data)

# print(type(user))
print(user)