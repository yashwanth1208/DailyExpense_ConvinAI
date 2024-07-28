import csv
from io import StringIO
from flask import Response

def format_amount(amount):
    return "{:.2f}".format(amount)

def download_balance_sheet(expenses):
    output = StringIO()
    writer = csv.writer(output)

    # Collect data for summary
    user_expense_summary = {}
    total_expenses = 0.0

    for expense in expenses:
        total_expenses += expense.amount
        for participant in expense.participants:
            user_name = participant.user.name if participant.user else 'Unknown'
            if user_name not in user_expense_summary:
                user_expense_summary[user_name] = 0.0

            if expense.split_method == 'equal':
                amount = expense.amount / len(expense.participants)
            elif expense.split_method == 'exact':
                amount = participant.amount
            elif expense.split_method == 'percentage':
                amount = (expense.amount * participant.percentage) / 100

            user_expense_summary[user_name] += amount

    # Write summary section
    writer.writerow(['Balance Sheet Summary'])
    writer.writerow(['User', 'Total Amount'])
    for user, amount in user_expense_summary.items():
        writer.writerow([user, format_amount(amount)])
    writer.writerow([])  # Empty line for separation

    # Write detailed expenses section
    writer.writerow(['Detailed Expenses'])
    writer.writerow(['Description', 'Total Amount', 'Split Method', 'User', 'Individual Amount'])
    for expense in expenses:
        for participant in expense.participants:
            user_name = participant.user.name if participant.user else 'Unknown'

            if expense.split_method == 'equal':
                amount = expense.amount / len(expense.participants)
            elif expense.split_method == 'exact':
                amount = participant.amount
            elif expense.split_method == 'percentage':
                amount = (expense.amount * participant.percentage) / 100

            writer.writerow([
                expense.description,
                format_amount(expense.amount),
                expense.split_method,
                user_name,
                format_amount(amount)
            ])

    response = Response(output.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=balance_sheet.csv'
    return response
