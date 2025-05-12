from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import (get_db)
from schemas import task as schemas
from core import task as core

router=APIRouter(prefix='/tasks', tags=['tasks'])

@router.post('/create_task', response_model=schemas.Task)
def create_task(task: schemas.Task, db:Session=Depends(get_db)):
    return  core.create_task(db, task)

@router.get('/', response_model=list[schemas.Task])
def read_tasks(db: Session=Depends(get_db)):
    return core.get_tasks(db)

@router.delete('/{task_id}', response_model=schemas.DeleteTask)
def delete_task(task_id:int, db:Session=Depends(get_db)):
    result=core.delete_task(db, task_id)
    if not result:
        raise HTTPException(status_code=404, detail='task not found')
    return {"detail":"task deleted"}

@router.patch('/{task_id}', response_model=schemas.Task)
def updated_task_status(task_id:int, status:bool, db:Session=Depends(get_db)):
    task=core.update_task_status(db, task_id, status)
    if not task:
        raise HTTPException(status_code=404, detail='task not found')
    return task
