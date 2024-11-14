from fastapi import FastAPI
from db.database import engine, Base
from app.routers import user_routers

# Create database tables based on the defined SQLAlchemy models
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI_Template",
    description="Template de FastAPI com autenticação JWT e estrutura modular.",
    version="1.0.0",
)

# Include user-related routes in the application with a specific prefix and tag
app.include_router(user_routers.router, prefix="/api/v1", tags=["Users"])
