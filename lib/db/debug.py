
# #!/usr/bin/env python3
from sqlalchemy import create_engine, select, text, func, cast, Float, Integer
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from models import City

Base = declarative_base()



engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()


