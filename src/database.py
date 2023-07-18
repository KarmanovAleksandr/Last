from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(settings.db_url)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
)


def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()