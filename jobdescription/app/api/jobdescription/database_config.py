# #POSTGRES
# from sqlalchemy import create_engine
# from databases import Database

# DATABASE_URL = "postgresql://postgres:pass@db:5432/job"

# engine = create_engine(DATABASE_URL)
# database = Database(DATABASE_URL)



##MYSQL
from sqlalchemy import create_engine
from databases import Database

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/test"

engine = create_engine(DATABASE_URL)
database = Database(DATABASE_URL)





# ##SQLIGHT
# from sqlalchemy import create_engine
# from databases import Database

# DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(DATABASE_URL)
# database = Database(DATABASE_URL)
