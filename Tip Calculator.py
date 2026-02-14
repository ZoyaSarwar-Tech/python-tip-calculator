print("WELCOME TO TIP CALCULATOR")

people=int(input("How many people want to share bill:?"))
tip_percentage=float(input("Enter your tip percentage:"))
bill=float(input("Enter your bill:"))
tip=bill*tip_percentage/100
total_bill=tip+bill
print("Your total bill is:",total_bill)
per_person=total_bill/people

round_off=input("You want to round off:(yes/no):")
if round_off=="yes":
    print("After round off is :",per_person)
elif round_off=="no":
    print("It left some amount")
print("Extra Information:")
if bill > 10000 and tip_percentage>5:
    print("you are so generous")
if people==1 and tip_percentage==0:
    print("you are eating alone")
if total_bill%people==0:
    print("Bill divide exactly")
else:
    print("Bill does not divide exactly")
if bill<0 and people<0:
    print("Invalid Input")
if bill==0 and people==0:
    print("Value must be greater than 0")


print("THANK YOU FOR USING TIP CALCULATOR")
