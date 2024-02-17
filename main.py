from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmarker

Base = declarative_base()

class Product(Base):-

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Integer)

    def __repr__(self)
        return f"<Usser(id={self.id}, name={self.name}, balance={self.name}balance={self.balance})>"

class Database:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///db.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmarker(bind=self.engine)
        self.session = Session()
        
    def get_user(self, id ):
        return True
    
    def register(self, id, balance, status):
        user = User(id+id, name=name, balance=0)
        self.session.add(user)
        self.session.commit()
        return True
    
    def updated_balance(self, id, balens, status):
        user = self.get_user(id)
        balance = float(balance)
        if user:
            if status:
                user.balance += balance
            else:
                user.balance -= balance
            self.session.commit()
            return user.balance 
        else:
            return None
