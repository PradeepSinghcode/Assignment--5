# Task 1: Create a Dictionary of Student Marks

D1 = {'A':50,'B':44}

#Taking input
a = input("Enter the student's name: ")
a.capitalize()

#Checking The Records
if a in D1:
    print(f"{a}'s marks:{D1[a]}")
else:
    print('student not found')