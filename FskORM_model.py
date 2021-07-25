from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost/SQL')
# engine = create_engine('postgres+postgres://root:@localhost:5432/SQL')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# objective of this project collecting college student information using SQL ORM
class DetailTable(Base):
    __tablename__ = 'Contact Details'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(30))
    phone_number = Column(Integer)
    location = Column(String(30))
    gmail = Column(String(30))

    def __init__(self, dict_data):
        self.name = dict_data['name']
        self.phone_number = dict_data['phone_number']
        self.location = dict_data['location']
        self.gmail = dict_data['gmail']


class LoginTable(Base):
    __tablename__ = 'Login Contact'

    id = Column(Integer, primary_key=True, unique=True)
    login = Column(String(30))
    password = Column(String(15))

    def __init__(self, login_data):
        self.login = login_data['user_login']
        self.password = login_data['password']


