def analyze_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense
    average = total / len(expenses) if expenses else 0
    highest = max(expenses) if expenses else 0
    print("Total expenses:", total)
    print("Average expense:", average)
    print("Highest expense:", highest)

expenses = [23.50, 19.99, 45.00, 12.75, 8.20]
analyze_expenses(expenses)
