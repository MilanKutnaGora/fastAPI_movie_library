from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, movie: schemas.MovieCreate):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie:
        for key, value in movie.dict().items():
            setattr(db_movie, key, value)
        db.commit()
        db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
    return db_movie

def add_favorite(db: Session, user_id: int, movie_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if user and movie:
        user.favorite_movies.append(movie)
        db.commit()
    return user

def remove_favorite(db: Session, user_id: int, movie_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if user and movie:
        user.favorite_movies.remove(movie)
        db.commit()
    return user

def get_user_favorites(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user.favorite_movies if user else []