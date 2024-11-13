from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Base
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# DATABASE_URL = "postgresql+psycopg2://username:password@localhost/task_manager"
DATABASE_URL = os.getenv("DATABASE_URL")
# Set up the database engine
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
