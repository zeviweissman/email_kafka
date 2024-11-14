import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_repr import RepresentableBase
from sqlalchemy_utils import database_exists, create_database, drop_database

load_dotenv(verbose=True)
PSQL_URL = os.environ['PSQL_URL']

Base = declarative_base(cls=RepresentableBase)
engine = create_engine(PSQL_URL)
_session_factory = sessionmaker(bind=engine)


def get_session():
    return _session_factory()

def create_data_base_if_not_exists():
    if not database_exists(engine.url):
        create_database(engine.url)

def drop_data_base_if_exists():
    if database_exists(engine.url):
        drop_database(engine.url)

def create_tabels_if_not_exists():
    Base.metadata.create_all(engine)


def initate_db():
    create_data_base_if_not_exists()
    create_tabels_if_not_exists()
