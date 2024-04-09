import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = f"postgresql://{os.getenv('DATABSE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@postgresserver/db"

engine = create_engine(DB_URL)

sessionlocal = sessionmaker(engine)

Base = declarative_base()