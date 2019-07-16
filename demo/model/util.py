from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('mysql+pymysql://root:root123@localhost:3306/test')

Session = sessionmaker(bind=engine)
session = Session()

