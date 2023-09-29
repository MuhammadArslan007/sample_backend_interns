from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from fastapi import Depends

DATABASE_URL = 'mysql+pymysql://root:12541254jA#@localhost:3306/user_progress'

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autoflush=False, autocommit= False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    except:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]  



