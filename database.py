from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()

connection_string = os.environ.get('DATABASE_URI')
engine = create_engine(connection_string)


def load_jobs():
    with engine.connect() as con:
        result = con.execute(text("SELECT * FROM jobs"))
        column_names = result.keys()  # Get column names
        jobs = [dict(zip(column_names, row)) for row in result.fetchall()]
        return jobs
