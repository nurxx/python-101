from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, update 

Base = declarative_base()

class Database:

    def __init__(self,db_name):
        self.db_name = db_name
        self.engine = create_engine('sqlite:///{}'.format(self.db_name),echo = True)
        Base.metadata.create_all(self.engine)

class Domain(Base):
    __tablename__ = 'URLS'

    id = Column(Integer,primary_key = True)
    domain = Column(String,nullable = True)
    server = Column(String,nullable = True)

    def __repr__(self):
        return "<Url(domain='%s', server='%s')>" % (self.domain, self.server)

