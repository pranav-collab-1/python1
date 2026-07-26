total_seats=40
available=total_seats
sold=0
print("The Available Seats in Bus:",available)
while available>0:
    tickets=int(input("Enter Number Of tickets to book:"))
    if tickets==0:
        print("Exiting Booking System")
    elif tickets<=available:
        available-=tickets
        sold+=tickets
        print(f"Your Booking Confirmed by booking-{tickets} and seats left {available}")
    else:
        print(f"Cannot book {tickets} only left seats are {available}")
    if available==0:
        print("Bus is Full No More Booking!")

    print("The number of seats booked:",sold)
    print("The number of tickets available:",available)
