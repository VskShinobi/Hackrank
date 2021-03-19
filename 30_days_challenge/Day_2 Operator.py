def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    tip = ((tip_percent/100) * meal_cost)
    tax = ((tax_percent/100)*meal_cost)
    total_cost = (meal_cost + tip + tax)
    print(round(total_cost))


solve(12.00,20,8)