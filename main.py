print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

realBill = totalBill + (tip / 100) * totalBill

eachPay = realBill/people
eachPay = round(eachPay, 2)
eachPay = "{:.2f}".format(eachPay)

print(f"Each person should pay: ${eachPay}")
