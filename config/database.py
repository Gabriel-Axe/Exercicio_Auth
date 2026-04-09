from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:lab123@localhost:5432/clinicadb"
#DATABASE_URL = "postgresql://postgres:lab123@localhost:5432/clinicadb"
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# ImportError: cannot import name 'get_session' from 'config.database' (D:\Files\exercise_auth\config\d atabase.py)

# def get_session():
#   return SessionLocal()
