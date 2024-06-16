from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,Field

app=FastAPI()





class Account(BaseModel):
    first_name: str  = Field(description="Firstname of the user")
    last_name: str = Field(description="lastname of the user")
    email: EmailStr = Field(description="Email of the user",examples=['demo@mail.com'])

@app.get("/accounts")
async def get_accounts(accounts:Account)-> list[Account]:
    return accounts


@app.post("/accounts")
async def save_account(account:Account):
    return account

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:<password>@localhost:5432/ott"
