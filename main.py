import vehicle

age = int(input("Enter the vehicle's age in years: "))
mpg = float(input("Enter the vehicle's MPG rating: "))
original_price = float(input("Enter the vehicle's original cost: "))

print(vehicle.Reliability(age))
print(vehicle.Fuel_Efficiency(mpg))

value = vehicle.Resale_Value(original_price, age)
print(f"Your car is now worth ${value:,.2f}")
