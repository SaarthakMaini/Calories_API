from pydantic import BaseModel,EmailStr
from typing import Optional

class UserRegistration(BaseModel):
    user_id : int
    username : str
    user_email: EmailStr
    password : str

class UserResponse(BaseModel):
    username : str
    user_email : EmailStr

class UserCreate(UserRegistration):
    password:str

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None