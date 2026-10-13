# Define variables for income and expenses
monthly_income = 3500
rent = 1200
groceries = 400
utilities = 150
transportation = 100
entertainment = 200
other_expenses = 250

def calculate_budget(income, rent, groceries, utilities, transportation, entertainment, other_expenses):
    total_expenses = rent + groceries + utilities + transportation + entertainment + other_expenses
    remaining_balance = income - total_expenses
    
    return total_expenses, remaining_balance

total_expenses, remaining_balance = calculate_budget(
    monthly_income, rent, groceries, utilities, transportation, entertainment, other_expenses
)

budget_summary = f"Total expenses: ${total_expenses}\nRemaining balance: ${remaining_balance}"
print(budget_summary)
