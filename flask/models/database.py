from sqlalchemy import create_engine ,text


username = "root"
password  = "#Machine1"
host = "127.0.1.1"
port = 3306 
database ="flask_db"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)
# with engine.connect() as conn:
    
