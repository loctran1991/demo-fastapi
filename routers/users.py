from app import models, schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db # pylint: disable=import-error


router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(new_user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    #hash password
    hashed_pwd = utils.hash(new_user.password)
    new_user.password = hashed_pwd
    
    created_user = models.User(**new_user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user


@router.get("/{id}", response_model=schemas.UserOut) ##
def get_users(id: str, db: Session = Depends(get_db)): # response: Response
    user_id = db.query(models.User).filter(models.User.id == id).first()
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {id} was not found")
    return user_id