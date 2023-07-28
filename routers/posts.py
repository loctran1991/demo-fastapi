from app import models, schemas, oauth2
from typing import List, Optional
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db # pylint: disable=import-error


router = APIRouter(
    prefix="/posts", #get prefix before sub url, exp: 127.0.0.0/posts
    tags=['Posts']
)

#use List[schemas.Post] because func will return list of dicts
#@router.get("/", response_model=List[schemas.Post]) #get all posts that were created by current user
@router.get("/", response_model=List[schemas.PostOut])
def get_all_posts(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = None):
    #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).limit(limit=limit).offset(skip).all()
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join( # pylint: disable=not-callable
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.get("/{id}", response_model=schemas.PostOut) ##
def get_posts(id: str, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)): # response: Response
    #post_id = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join( # pylint: disable=not-callable
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {id} was not found")
    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(new_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    #created_post = models.Post(title=new_post.title, content=new_post.content, published=new_post.published)
    #we have another way to get post from actions POST with more clean
    created_post = models.Post(owner_id=current_user.id, **new_post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: str, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    
    if not deleted_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} was not found")
    
    if deleted_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perform actions")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()
    

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: str, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    updated_post = db.query(models.Post).filter(models.Post.id == id)
    if not updated_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} was not found")
    
    if updated_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perform actions")
    
    updated_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return {"Message":"Updated Post"}