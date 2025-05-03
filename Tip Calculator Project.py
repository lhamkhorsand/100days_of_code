print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percent_of_tip = tip / 100
total_tip = bill * percent_of_tip
total_bill = total_tip + bill
bil_per_person = total_bill / people
final_amount = round((bil_per_person) , 2)
print(f"Each person should pay: ${final_amount}")

