from sqlalchemy.orm import Session
from tasks import model as models, schemas as schemas


def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.Task):
    db_task=models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id:int):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()  # type: ignore
    if task:
        db.delete(task)
        db.commit()
        return True
    return None

def update_task_status(db: Session, task_id:int, status:bool):
    task=db.query(models.Task).filter(models.Task.id==task_id).first()  # type: ignore
    if task:
        task.completed=status
        db.commit()
        return task
    return None
