def Reliability(age):
    if age > 10:
        return "Your car is unreliable."
    else:
        return "Your car is reliable."


def Fuel_Efficiency(mpg):
    if mpg >= 30:
        return "Your car is fuel-efficient."
    else:
        return "Your car is not fuel efficient."


def Resale_Value(original_price, age):
    depreciation_rate = 0.03
    depreciation_amount = original_price * (depreciation_rate * age)
    current_value = original_price - depreciation_amount
    return current_value
