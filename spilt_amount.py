# 11. Suppose you often go to a restaurant with friends and need to split the bill. Write a
# program to calculate the split amount.

bill_amount = 3540

total_people = 5

spilt_amount = (bill_amount) / (total_people)

print(f"Each person should py : Rs : {spilt_amount} ")
print("\n")


# user Interface

total_bill_amount = float(input("Enter the total bill amount : "))

totals_people = int(input("Enter the total people : "))

spilt_bill_amount = (total_bill_amount)  / totals_people

print(f"Each person should pay : Rs : {spilt_bill_amount}")

