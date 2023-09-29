from sqlalchemy import Integer, String, Column, Float
from database import Base
from database import engine
Base.metadata.create_all(bind=engine)

class userStudy(Base):
    __tablename__ = 'user_study'
    study_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(Integer,primary_key=True)
    paths = Column(String(150))
    category = Column(String(150))
    unit = Column(String(150))
    section = Column(String(150))
    topic = Column(String(150))
    topic = Column(String(150))
    status = Column(Float)
    
    
