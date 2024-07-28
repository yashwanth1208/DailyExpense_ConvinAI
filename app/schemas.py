from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    name = fields.Str(required=True)
    mobile_number = fields.Str(required=True)

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    amount = fields.Float(required=True)
    split_method = fields.Str(required=True, validate=validate.OneOf(['equal', 'exact', 'percentage']))
    user_id = fields.Int(required=True)
    participants = fields.Nested('ParticipantSchema', many=True)

class ParticipantSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    expense_id = fields.Int(required=True)
    amount = fields.Float()
    percentage = fields.Float()
