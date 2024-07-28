def calculate_equal_split(amount, participants):
    split_amount = amount / len(participants)
    return {participant: split_amount for participant in participants}

def calculate_exact_split(amounts, participants):
    return {participants[i]: amounts[i] for i in range(len(participants))}

def calculate_percentage_split(amount, percentages, participants):
    return {participants[i]: (percentages[i] / 100) * amount for i in range(len(participants))}
