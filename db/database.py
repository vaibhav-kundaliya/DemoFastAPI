import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os.path import join, dirname
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

DB_URL = f"postgresql://{os.getenv('DATABSE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@localhost:5432"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()