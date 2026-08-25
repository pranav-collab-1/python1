##my_list = ["a","b","a",1,2,3,1,2,3,3]
##unique = list(set(my_list))
##print(unique)

##my_list = ["a", "b", "a", 1, 2, 3, 1, 2, 3, 3]
##
##duplicates = []
##
##for item in my_list:
##    if my_list.count(item) > 1 :
##        duplicates.append(item)
##print(duplicates)


##a=input("Enter string1:")
##b=input("Enter string2:")
##if sorted(a) == sorted(b):
##    print("These two strings are anagram")
##else:
##    print("Not anagram!")


##list = [1, 2, 3, 3, 2, 5, 6, 7]
##duplicates = []
##
##for x in list:
##    if list.count(x) > 1:
##        if x not in duplicates:
##            duplicates.append(x)
##
##print(duplicates)

##cabs = [(101, "raj", "sedan", 10),
##        (102, "tej", "suv", 20),
##        (103, "sai", "mini suv", 5)]
##a = int(input("Enter the cab Id: "))
##b = int(input("Enter the trip distance: "))
##for cab in cabs:
##    if a == cab[0]:
##        total_price = b * cab[3]
##        print(f"Your cab is available with car id {a} and total price is ₹{total_price}")
##        break
##else:
##    print("Cab is not available")

##students={}
##num = int(input("Enter no of students:"))
##
##for i in range(num):
##    print(f"students {i+1}:")
##    name=input("Enter student name:")
##    num_sub=int(input("Enter no of subjects"))
##    marks_dic={}
##    for j in range(num_sub):
##        subject = input(f"Enter subject {j+1}:")
##        marks=int(input("Enter subject marks:")
# Question 1
##sentence = input("Enter a sentence: ")
##a = {}
##for ch in sentence:
##    if ch in a:
##        a[ch] += 1
##    else:
##        a[ch] = 1
##for ch,count in a.items():
##    print(f"'{ch}': {count}")
##sentence = input("Enter a sentence: ")
##v = ['a','e','i','o','u','A','E','I','O','U']
##vowel = 0
##consonant = 0
##for i in sentence:
##    if i in v:
##        vowel += 1
##    else:
##        consonant += 1
####print("Vowels:",vowel,"\nConsonants:",consonant)
##my_list = ["a","b","a",1,2,3,1,2,3,3]
##unique = list(set(my_list))
##print(unique)
##
##
##new1 = [1,1,2,3,3,4,5]
##dup = []
##for i in new1:
##    if new1.count(i)>1:
##        dup.append(i)
##print(dup)
##A = {'a','b','c'}
##B = {'b','c','d'}
##one = A & B
##two = A - B
##three = A | B
##four = B - A
##five = A or B
##print(one,two,three,four,five)
##matrix = [[1, 2, 3],[4, 5, 6]]
##transpose = []
##for i in range(len(matrix[0])):
##    new_row = []
##    for row in matrix:
##        new_row.append(row[i])
##    transpose.append(new_row)
##print(transpose)

##a = input("Enter first string: ")
##b = input("Enter second string: ")
##if sorted(a) == sorted(b):
##    print("Anagrams")
##else:
##    print("Not an Anagram")

cabs = [
    (101,"Raju","Bike",12),
    (102,"Ramu","Car",25),
    (103,"Ravi","Luxury",60)
]

# Display available services
##dist = float(input("Enter trip distance: "))
##cab_id = int(input("Enter cab ID: "))
##total = 0
##selected = False
##for i in cabs:
##    if i[0]==cab_id:
##        total = dist*i[-1]
##        selected = True
##        break
##
##if selected:
##    print("\n-----Booking Summary-----\n")
##    print("Cab ID:",cab_id,"\nDriver:",i[1],"\nVehicle:",i[2],"\nRate per Kilometer:",i[-1],"\nTotal cost:",total)
##else:
##    print("Booking failed. Invalid Car ID")

report = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name of the student: ")
    sub = int(input("Enter number of subjects: "))
    marks_dict = {}
    for j in range(sub):
        sub_name = input("Enter subject name: ")
        sub_marks = int(input("Enter marks: "))
        marks_dict[sub_name] = sub_marks
    report[name] = marks_dict
print("\n---STUDENT REPORT CARD---\n")
for name,subjects in report.items():
    print("Student name:",name)
    total = sum(subjects.values())
    average = total/len(subjects)
    if average>=90:
        grade = "A+"
    elif average >=80:
        grade = "A"
    elif average >=70:
        grade = "B"
    elif average >=50:
        grade = "C"
    elif average >=35:
        grade = "D"
    else:
        grade = "F"
    print("Subjects and marks:")
    for subject,marks in subjects.items():
        print(f"{subject}:{marks}")
    print("Total marks:",total)
    print("Average marks:",average)
    print("Grade:",grade)







