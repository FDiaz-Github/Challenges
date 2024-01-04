import os
from sqlalchemy import create_engine, Column, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def create_session(database_url=os.environ.get('DATABASE_URL')):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    db_session = sessionmaker(bind=engine)
    return db_session()


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    amount = Column(Float)

    def __repr__(self):
        return f"<Transaction(id={self.id}, date={self.date}, amount={self.amount})>"
