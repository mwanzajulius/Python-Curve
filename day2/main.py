#calculating a bill. total amount, tip %, how many people then each
print("Welcome to the tip calculator")
bill=float(input("How much is your bill? $"))
tip=int(input("How much is your tip? 10, 15, 20 "))
number=int(input("How many are you? "))
if tip== 10:
    bill=bill*1.10
elif tip==15:
    bill=bill*1.15
elif tip==20:
    bill=bill*1.20
else:
    bill=bill*1.05
total=bill /number
billPerPerson=round(total,2) #rounding off function
print(f"Each person should pay ${billPerPerson}")
