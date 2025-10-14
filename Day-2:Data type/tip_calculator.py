print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give?  10, 12, or 15?"))
bill_after_bill=tip*total_bill + total_bill
split=int(input("How many people to split the bill?"))
bill_per_person=round(bill_after_bill/split,2)
print(f"Each person should pay:  ${bill_per_person}")
