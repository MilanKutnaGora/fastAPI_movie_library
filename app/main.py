from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db=db, movie=movie)

@app.put("/movies/{movie_id}", response_model=schemas.Movie)
def update_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.update_movie(db, movie_id, movie)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.delete("/movies/{movie_id}", response_model=schemas.Movie)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.delete_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.post("/users/{user_id}/favorites/{movie_id}", response_model=schemas.User)
def add_favorite(user_id: int, movie_id: int, db: Session = Depends(get_db)):
    db_user = crud.add_favorite(db, user_id, movie_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User or Movie not found")
    return db_user

@app.delete("/users/{user_id}/favorites/{movie_id}", response_model=schemas.User)
def remove_favorite(user_id: int, movie_id: int, db: Session = Depends(get_db)):
    db_user = crud.remove_favorite(db, user_id, movie_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User or Movie not found")
    return db_user

@app.get("/users/{user_id}/favorites", response_model=list[schemas.Movie])
def get_user_favorites(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_favorites(db, user_id)