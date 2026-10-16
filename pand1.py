import pandas as pd
s = pd.Series([1, 3, 5, None, 6, 8],name="marks",index=['a','b','c','d','e','f'])

print(s)
students = pd.DataFrame({'name':['Alice','Bob','Charles','David','Edward','Frank'],'marks':[85,90,78,92,88,95]},index=['a','b','c','d','e','f'])
print(students)
print(students.shape)
