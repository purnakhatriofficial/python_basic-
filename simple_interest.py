# Write a program to find the simple interest. 

principle_amount = 50000

interest = 3

time = 12

simple_interest = (principle_amount * interest * time) / 100

print(f"Total amount is : {simple_interest}")

print("\n")

# Write a program to find the simple interest.  User interface 

principle_amounts = int(input("Enter The Ammount : "))

time_of_years = int(input("Enter The Number of Years : "))

interest_rate= int(input("Enter The Rate Of interest : "))

simple_interest_calculator = (principle_amounts * time_of_years * interest_rate) / 100

print(f"The total InterestIs : {simple_interest_calculator}")

