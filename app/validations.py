def validate_percentage_split(percentages):
    if sum(percentages) != 100:
        return False
    return True
