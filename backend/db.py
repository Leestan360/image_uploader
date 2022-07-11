from database import engine, Base
from models import User, Image


Base.metadata.create_all(bind=engine)