import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables


DSN = "postgresql://postgres:4652732-oP@localhost:5432/bookdb"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)
    print(data)

session.close()
