days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
temp=[]
for i in range(7):
    t=float(input("Enter the temperature of " + days[i]  ))
    temp.append(t)
max_temp=max(temp)
min_temp=min(temp)
max_day=days[temp.index(max_temp)]
min_day=days[temp.index(min_temp)]
print(f"Maximum temparature in week {max_temp} on {max_day}")
print(f"Minimum temparature in week {min_temp} on {min_day}")
