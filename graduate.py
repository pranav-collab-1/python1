## W.A.P Program where user will enter his/her registration number and program will
## display his/her year of B. Tech. completion with specialization.
## Also display a ‘Invalid roll number’
## message if student is having roll no 0000 from any year any specialization. 
a=int(input("Enter your Registration Number:"))
if (a<23000)and (a>22000):
    print("Your graduation will be in the year:2026")
elif (a<24000)and (a>23000):
    print("Your graduation will be in the year:2027")
elif (a<25000)and (a>24000):
    print("Your graduation will be in the year:2028")
elif (a<26000)and (a>25000):
    print("Your graduation will be in the year:2029")
else:
    print("Not a valid registration number!!!")
