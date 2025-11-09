import os
import time
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.exc import OperationalError

# Get DATABASE_URL from environment
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise NotImplementedError("DATABASE_URL is not set")

DATABASE_URL = DATABASE_URL.replace("postgress://", "postgres+psycopg://")

def wait_for_db(url, retries=10, delay=3):
    """Wait for the PostgreSQL database to be ready before connecting."""
    engine = create_engine(url)
    for i in range(retries):
        try:
            with engine.connect():
                print("Database is ready!")
                return engine
        except OperationalError:
            print(f"Database not ready, retrying in {delay}s...")
            time.sleep(delay)
    raise RuntimeError("Database not available after several retries")

# Create engine after DB is ready
engine = wait_for_db(DATABASE_URL)

# Database models initialization
def init_db():
    print("Initializing database...")
    SQLModel.metadata.create_all(engine)

# Dependency for API routes
def get_session():
    with Session(engine) as session:
        yield session
