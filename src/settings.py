import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    server_host: str = "0.0.0.0"
    server_port: int = 8000

    db_server: str = os.environ.get("DB_HOST")
    db_name: str = os.environ.get("DB_DATABASE")
    db_username: str = os.environ.get("DB_USERNAME")
    db_password: str = os.environ.get("DB_PASSWORD")
    db_url: str = f"postgresql://{db_username}:{db_password}@{db_server}/{db_name}"

    jwt_secret: str = os.environ.get("JWT_SECRET")
    jwt_algoritm: str = "HS256"
    jwt_expiation: int = 3600

    redis_host = os.environ.get("REDIS_HOST")
    redis_port = os.environ.get("REDIS_PORT")
    redis_url = f"redis://{redis_host}:{redis_port}"

    rabbit_host = os.environ.get("RABBIT_HOST")
    rabbit_url = f"amqp://guest:guest@{rabbit_host}:5768"

settings = Settings()
