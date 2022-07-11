from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('postgresql://postgres:Stano360@localhost/image_uploader',
    echo = True
)

Base = declarative_base()

Session = sessionmaker()