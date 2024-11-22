# Suppose your distance to the office from home is 25 km, and you travel at 40 km
# per hour. Write a program to calculate the time taken to reach the office.



distance_km = 25

speed_km = 40

time_hours = (distance_km) / (speed_km)

# Conver time to minute

time_minutes = time_hours * 60

print(f"The time taken to reach the office : {time_hours} hours or {time_minutes} minutes :")

print("\n")



# user interface 

distance_kilometer = float(input("Enter your travel distance in kilometers : "))

speed_kilometer = int(input(" Enter your trip in kilometers : "))

time_to_hourse = (distance_kilometer) / (speed_kilometer)

#conver time to minute 

times_minutes = time_to_hourse * 60

print(f"The time taken to reach the office : {time_to_hourse} hours or : {times_minutes} minutes ")