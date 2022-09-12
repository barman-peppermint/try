from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id : int | None = None
    name = "Vijay Barman"
    signup_ts : datetime | None = None
    age : int


external_data = {
    "id" : "0",
    "signup_ts" : "2020-06-10 12:22",
    "age" : 22
}


user = User(**external_data)
print(user)

print(user.age)