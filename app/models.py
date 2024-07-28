from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    mobile_number = Column(String, unique=True)

    expenses = relationship("Expense", back_populates="user")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Float)
    split_method = Column(Enum('equal', 'exact', 'percentage', name='split_method'))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="expenses")
    participants = relationship("Participant", back_populates="expense")

class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    expense_id = Column(Integer, ForeignKey('expenses.id'))
    amount = Column(Float)
    percentage = Column(Float)

    user = relationship("User")
    expense = relationship("Expense", back_populates="participants")
