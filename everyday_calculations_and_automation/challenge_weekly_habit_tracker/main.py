def track_habit(daily_values):
    total = 0
    for value in daily_values:
        total += value
    av = total / len(daily_values)
    print(f"Weekly Total:{total}")
    print(f"Weekly Average:{av}") 
    

# Sample calls
track_habit([8, 7, 6, 9, 8, 7, 10])
track_habit([2, 2, 2, 2, 2, 2, 2])
