from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# NOTE: Importation of DB models must occur AFTER declaration of Base.
# NOTE: No longer necessary after using alembic migrations
#  from .models.item import Item
#  from .models.user import User

#  Base.metadata.create_all(bind=engine)
