from flask import Blueprint, request, jsonify
from . import db
from .models import User, Expense, Participant
from .schemas import UserSchema, ExpenseSchema, ParticipantSchema
from .balance_sheet import download_balance_sheet

# Define the blueprint
bp = Blueprint('routes', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
expense_schema = ExpenseSchema()
expenses_schema = ExpenseSchema(many=True)

# User Endpoints
@bp.route('/user', methods=['POST'])
def create_user():
    email = request.json['email']
    name = request.json['name']
    mobile = request.json['mobile']
    new_user = User(email=email, name=name, mobile=mobile)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@bp.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# Expense Endpoints
@bp.route('/expense', methods=['POST'])
def add_expense():
    description = request.json['description']
    amount = request.json['amount']
    split_method = request.json['split_method']
    user_id = request.json['user_id']
    participants_data = request.json.get('participants', [])

    new_expense = Expense(description=description, amount=amount, split_method=split_method, user_id=user_id)
    db.session.add(new_expense)
    db.session.commit()

    # Add participants
    for participant in participants_data:
        participant_user_id = participant['user_id']
        participant_amount = participant.get('amount')
        participant_percentage = participant.get('percentage')
        new_participant = Participant(user_id=participant_user_id, expense_id=new_expense.id, amount=participant_amount, percentage=participant_percentage)
        db.session.add(new_participant)

    db.session.commit()

    return expense_schema.jsonify(new_expense)

@bp.route('/expense/user/<user_id>', methods=['GET'])
def get_user_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return expenses_schema.jsonify(expenses)

@bp.route('/expense', methods=['GET'])
def get_all_expenses():
    expenses = Expense.query.all()
    return expenses_schema.jsonify(expenses)

@bp.route('/balance_sheet', methods=['GET'])
def get_balance_sheet():
    expenses = Expense.query.options(db.joinedload(Expense.participants).joinedload(Participant.user)).all()
    return download_balance_sheet(expenses)

