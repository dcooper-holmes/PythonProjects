
print("Welcome to the Tip Calculator.")

totalBill = float(input("What was the total bill $"))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100
numPeople = int(input("How many people to split the bill ? "))

finalTip = totalBill * tipPercentage
finalBill = totalBill + finalTip

newTotalBill = round(finalBill / numPeople, 2)

print(f"Each person should pay: ${newTotalBill}")