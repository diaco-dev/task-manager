from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from user import services as core, schemas as schemas

router=APIRouter(prefix='/users', tags=['users'])

@router.post('/create_user', response_model=schemas.User)
def create_usr(user: schemas.UserCreate, db:Session=Depends(get_db)):
    return core.create_user(db, user)

@router.get('/', response_model=list[schemas.User])
def read_users(db: Session=Depends(get_db)):
    return  core.get_user(db)

@router.delete('/{user_id}', response_model=schemas.DeleteUser)
def delete_user(user_id:int ,db:Session=Depends(get_db)):
    result=core.delete_user(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail='email not found')
    return {'detail':'email deleted'}


@router.patch('/{user_id}', response_model=schemas.Message)
def update_user_password(user_id:int,
                         password: schemas.ChangePassword,
                         db:Session=Depends(get_db)):
    return core.change_user_password(
        user_id=user_id,
        db=db,
        current_password=password.current_password,
        new_password=password.new_password
    )


