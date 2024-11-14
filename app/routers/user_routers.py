from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from db.database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.UserResponse:
    """
    Creates a new user in the database.

    Args:
        user (schemas.UserCreate): The data required to create a new user, including username, email, and password.
        db (Session): Database session dependency.

    Returns:
        schemas.UserResponse: The created user data, formatted as defined by the UserResponse schema.

    Raises:
        HTTPException: If there is an error during user creation.
    """
    db_user = models.User(
        username=user.username, 
        email=user.email, 
        hashed_password=user.password  # Assumes password is already hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
