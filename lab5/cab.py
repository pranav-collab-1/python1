cabs = [
 (101,"Raju","Bike",12),
 (102,"Ramu","Car",25),
 (103,"Ravi","Luxury",60)
]
# Display available services
dist = float(input("Enter trip distance: "))
cab_id = int(input("Enter cab ID: "))
total = 0
selected = False
for i in cabs:
 if i[0]==cab_id:
 total = dist*i[-1]
 selected = True
 break
if selected:
 print("\n-----Booking Summary-----\n")
 print("Cab ID:",cab_id,"\nDriver:",i[1],"\nVehicle:",i[2],"\nRate per
Kilometer:",i[-1],"\nTotal cost:",total)
else:
 print("Booking failed. Invalid Car ID")
