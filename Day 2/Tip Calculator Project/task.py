print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip/100
total_with_tip = bill +(bill*tip_percent)
per_person = total_with_tip/people

print(f"your tip per person is{per_person} dollars")
