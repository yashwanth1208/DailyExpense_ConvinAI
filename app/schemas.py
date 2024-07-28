from . import ma
from .models import User, Expense, Participant

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class ParticipantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Participant

class ExpenseSchema(ma.SQLAlchemyAutoSchema):
    participants = ma.Nested(ParticipantSchema, many=True)

    class Meta:
        model = Expense
