from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .crud import get_account,get_accounts,create_account
from .db import SessionLocal, engine
from . import crud, models, schemas


models.Base.metadata.create_all(bind=engine)


app=FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/accounts",  response_model=list[schemas.Account])
async def get_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
      accounts = crud.get_accounts(db, skip=skip, limit=limit)
      return accounts


@app.post("/accounts",  response_model=schemas.Account)
async def save_account(account: schemas.Account, db: Session = Depends(get_db)):
    return crud.create_account(db=db, account=account)


@app.get("/Select_Movie", response_model=list[schemas.Select_Movie])
async def get_movies(skip:int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies =





# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:<password>@localhost:5432/ott"
