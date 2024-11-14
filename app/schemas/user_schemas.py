from pydantic import BaseModel

class UserBase(BaseModel):
    """
    Shared attributes for a user, used as a base for other schemas.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
    """
    username: str
    email: str

class UserCreate(UserBase):
    """
    Schema for creating a new user, extending UserBase.

    Attributes:
        password (str): The password for the new user.
    """
    password: str

class UserResponse(UserBase):
    """
    Schema for the response model of a user, extending UserBase.

    Attributes:
        id (int): The unique identifier of the user.
        
    Config:
        orm_mode (bool): Enables ORM mode for compatibility with SQLAlchemy models.
    """
    id: int

    class Config:
        orm_mode = True
