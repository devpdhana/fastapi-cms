from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi_cms.repositories.schemas.Base import Base
from fastapi_cms.repositories.schemas.Ticket import Ticket

URL = "postgresql://postgres:Devpds$3001@db.fissfdeletczfwcmdvra.supabase.co:5432/postgres"
engine = create_engine(url=URL)

connection = sessionmaker(bind=engine)


def get_db():
    with connection() as db:
        yield db


Base.metadata.create_all(bind=engine)
