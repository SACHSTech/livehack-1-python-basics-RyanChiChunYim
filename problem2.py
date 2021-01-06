'''
-------------------------------------------------------------------------------
Name:		problem2
Purpose:	To distribute the amount of chicken to students evenly and to give Mr. Fabroa the rest of the chicken

Author:	Yim.R

Created: 07/12/2020
------------------------------------------------------------------------------
'''

#input the the pieces of popeyes chicken and students
chicken = float(input("Enter the number of chicken:"))
students = float(input("Enter the number of students:"))
#Distribute the number of chicken evenly among students and teacher

distribution = chicken//students
fabs_chicken = distribution%students
#Output should be the evenly distributed chicken to everyone
print ("This is how many pieces of chicken the students will each get: " + str(distribution) + " This is how many pieces of chicken Mr. Fabroa will get:" + str(fabs_chicken))
