from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas



def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return  db.query(models.Account).offset(skip).limit(limit).all()

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def create_account(db: Session, account: schemas.Account):
    created_time = datetime.now()
    db_account = models.Account(email=account.email, first_name = account.first_name, last_name = account.last_name,created_at=created_time)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account



