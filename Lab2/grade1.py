while True:
 a=int(input("Enter Your Marks:"))
 if (a<100)and(a>=90):
     print("The grade is A+ and marks ontained:",a)
     print("Remark:Outstanding")
     print("Result:Pass")
 elif (a<90)and(a>=75):
     print("The grade is A and marks ontained:",a)
     print("Remark:Excellent")
     print("Result:Pass")
 elif (a<75)and(a>=60):
     print("The grade is B  and marks ontained:",a)
     print("Remark: Good")
     print("Result:Pass")
 elif (a<60)and(a>=50):
     print("The grade is C and marks ontained:",a)
     print("Remark:Average")
     print("Result:Pass")
 elif (a<50)and(a>=40):
     print("The grade is D and marks ontained:",a)
     print("Remark:Pass")
     print("Result:Pass")
 else:
     print("grade is F")
     print("Remark:Fail")
        
        
