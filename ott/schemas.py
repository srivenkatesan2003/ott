from datetime import datetime
from pydantic import BaseModel,EmailStr,Field


class Account(BaseModel):

    first_name: str  = Field(description="Firstname of the user")
    last_name: str = Field(description="lastname of the user")
    email: EmailStr = Field(description="Email of the user",examples=['demo@mail.com'])
    created_at:datetime=Field(description="date of the user")



class Select_Movie(BaseModel):
    user_name: str =Field(description="user name" ,min_length=3,max_length=30)
    movies: str= Field(description="movie name")
    category: int =Field(description ="age")
    year: int =Field(description="film name")

    