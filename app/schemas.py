from . import ma
from .models import User, Expense

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class ExpenseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
