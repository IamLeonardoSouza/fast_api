from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    """
    Represents a user entity in the database.

    Attributes:
        id (int): Primary key identifier for the user.
        username (str): Unique username for the user.
        email (str): Unique email address of the user.
        hashed_password (str): Hashed password for the user.
    """
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True)
    email: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)
