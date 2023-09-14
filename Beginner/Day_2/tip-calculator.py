def tip_calc():
    print("Welcome to the tip calculator.")
    total = float(input("What was the total bill? $"))
    split = float(input("How many people to split the bill? "))
    percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
    if percent == 10 or percent == 12 or percent == 15:
        result = (total + (total*(percent/100)))/split
        print(f"Each person should pay: ${result:.2f}")
        return 1
    else:
        print("Invalid tip option. Please enter 10, 12 or 15 only")
        return 0

tip_calc()
