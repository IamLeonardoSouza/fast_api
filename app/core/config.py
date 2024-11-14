from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Configuration settings for the FastAPI application.

    Attributes:
        app_name (str): The name of the application, with a default value of "FastAPI_Template".
        database_url (str): The URL for connecting to the database.
    """
    app_name: str = "FastAPI_Template"
    database_url: str

    class Config:
        """
        Configuration class for Pydantic settings.

        Attributes:
            env_file (str): Specifies the path to the environment file for loading variables.
        """
        env_file: str = ".env"

# Initialize settings with environment variables loaded from `.env` file.
settings: Settings = Settings()
