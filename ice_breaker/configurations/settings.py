import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv


load_dotenv(os.path.join(find_dotenv(".env")))


class Settings(BaseSettings):
    LINKEDIN_USERNAME: str = os.getenv("LINKEDIN_USERNAME")
    LINKEDIN_PASSWORD: str = os.getenv("LINKEDIN_PASSWORD")


settings = Settings()
