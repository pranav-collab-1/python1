##A company decided to give bonus of 5% to employees
##if his/her year of service is more than 5 years.
##Ask user for their salary and year of service and W.A.P to print the net bonus amount and total salary of employee. 
a=int(input("Enter Your Salary:"))
b=int(input("Enter year of service:"))
c=0.05*a
if b>5:
    print("The net Salary is:",a+c)
else:
    print("The net salary is:",a)
    
      
