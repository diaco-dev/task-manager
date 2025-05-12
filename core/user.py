from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import user as models
from schemas import user as schemas
from core.pwd import verify_password, get_password_hash


def get_user(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user:schemas.UserCreate):
    user_exist=db.query(models.User).filter(models.User.email==user.email).first()      # type: ignore
    if user_exist:
        raise HTTPException(status_code=400, detail='email already exist')

    hashed_password=get_password_hash(user.password)

    db_user=models.User(email=user.email,
                        username=user.username,
                        hashed_password=hashed_password,)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        "id":db_user.id,
        "email":db_user.email,
        "username":db_user.username,
    }


def delete_user(db:Session, user_id:int):
    user=db.query(models.User).filter(models.User.id==user_id).first()    # type: ignore
    if user:
        db.delete(user)
        db.commit()
        return True
    return None


def change_user_password(db:Session, user_id:int, current_password: str, new_password: str):
    db_user=db.query(models.User).filter(models.User.id==user_id).first()      # type: ignore

    if not db_user:
        raise HTTPException(status_code=404, detail='user not found')

    if not verify_password(current_password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail='incorrect current password')

    if verify_password(new_password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail='new password must be different')

    hashed_new_password=get_password_hash(new_password)
    db_user.hashed_password=hashed_new_password

    db.commit()
    db.refresh(db_user)
    return {'message':'password updated successfully'}