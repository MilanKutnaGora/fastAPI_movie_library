from pydantic import BaseModel
from typing import List, Optional

class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    favorite_movies: List[Movie] = []

    class Config:
        orm_mode = True