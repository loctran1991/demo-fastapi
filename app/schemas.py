from pydantic import BaseModel, EmailStr, conint # pylint: disable=no-name-in-module
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
        
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

#this class is used to reponse the request
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True
        
#this class is used to reponse the request
class PostOut(BaseModel):
    Post: Post
    votes: int #votes must match with lable in post.py query
    class Config:
        orm_mode = True   
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str

    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)