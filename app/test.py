from sqlalchemy import create_engine
import urllib.parse

host_db = '192.168.1.100:5432'
postgres_user = 'py_fastapi'
postgres_db = 'py_fastapi'
postgres_pwd = urllib.parse.quote_plus("$_Luke%1991")  

#SQLALCHEMY_DATABASE_URL = 'postgresql://fastapi-python:"$_Luke%1991"@192.168.1.100/fastapi-python'

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{postgres_user}:{postgres_pwd}@{host_db}/{postgres_db}"
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)