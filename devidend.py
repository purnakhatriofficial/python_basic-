# Write a program to find the quotient and remainder of two integers.

devidend = int(input("Enter the devidend : "))
divisor = int(input("Enter the Divisor : "))

quitient = devidend // divisor

reminder = devidend % divisor

print(f"The quitient is : {quitient}")
print(f"The reminder is : {reminder}")