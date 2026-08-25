##import numpy as np
##print (" Arange :", np . arange (0 , 12 , 2) )
##print (" Linspace (5 values between 0 and 1):", np . linspace (0 , 1 , 5) )
import numpy as np

##arr = np . array ([[11 , 22 , 33] ,
## [44 , 55 , 66] ,
## [77 , 88 , 99]])
##
##print (" Array :\n", arr )
##print (" Number of dimensions ( ndim ):", arr . ndim )
##print (" Shape :", arr . shape )
##print (" Total elements ( size ):", arr . size )
##print (" Data type :", arr . dtype )
##print (" Bytes per element :", arr . itemsize )
##print (" Total memory ( nbytes ):", arr . nbytes )
##a = np . array ([[10 , 20 , 30 , 40] ,
## [50 , 60 , 70 , 80] ,
## [90 , 100 , 110 , 120]])
##print ("Sub - array ( rows 0 -1 , columns 1 -3) :\n", a [0:2 , 1:3])
##print(a>60)
##A = np . array ([[1 , 2] , [3 , 4]])
##B = np . array ([[5 , 6] , [7 , 8]])
##print (" Matrix multiplication (dot product ):\n", A @ B )
##print(A*B)
##arr = np . arange (1 , 13)
##reshaped = arr . reshape (3 , 4)
##print (" Flattened :", reshaped . flatten () )
##print (" Reshape with -1 ( auto calculate ):\n", arr . reshape (2 , -1) )
import numpy as np
import time
np . random . seed (7) # for reproducible results

 # Simulate marks of 5 students in 4 subjects
##marks = np . random . randint (40 , 100 , size =(5 , 4) )
##print (" Marks of 5 students (4 subjects ):\n", marks )
##
##print ("\ nAverage marks of each student :", marks . mean ( axis =1) . round (2) )
##print (" Average marks in each subject :", marks . mean ( axis =0) . round (2) )
##print (" Highest mark overall :", marks .max () )
##print (" Students who scored above 80 in any subject :\n", marks [ marks > 80])
##
## # Add 5 bonus marks to all
##bonus_marks = marks + 5
##print ("\ nAfter adding 5 bonus marks :\n", bonus_marks )
size = 1000000
a = np . random . rand ( size )
b = np . random . rand ( size )

 # Slow way - Python loop
start = time . time ()
result_loop = np . zeros ( size )
for i in range ( size ) :
 result_loop [ i ] = a [ i ] + b [ i ]
print (" Loop time :", round ( time . time () - start , 4) , " seconds ")

 # Fast way - Vectorized
start = time . time ()
result_vec = a + b
print (" Vectorized time :", round ( time . time () - start , 4) , " seconds ")

print (" Results are equal :", np . allclose ( result_loop , result_vec ) )
