file = open("D:\\student_record\\mini_project.txt","a")
student_name = input(f"Enter the name of student: ")
roll_no = int(input("Roll No:  "))

print('enter subject marks:')
english = float(input("English Marks: "))
mathematics = float(input("Mathematics Marks: "))
python = float(input("Computer Sciences Marks: "))
electronics = float(input('electronics marks: '))

#------------------marking section------------------------#

if  0 <= english <= 100 and 0 <= mathematics <= 100 and 0 <= python <= 100 and 0 <= electronics <= 100 :
    total = english+mathematics+python+electronics
    percentage = (total/4)
    print(f"\nTotal Marks: {total}")
    print(f"Percentage: {percentage}%")
else:
    print("\nInvalid Input. Please enter a number between 0 to 100.")

#------------------grade section------------------------#    

if  percentage >=90:
    grade = "A+"
elif percentage >=85:
    grade = "A"
elif percentage >=80:
    grade = "B+"
elif percentage >=75:
    grade = "B"
elif percentage >=70:
    grade = "B-"
elif percentage >=65:
    grade = "C+"
elif percentage >=60:
    grade = "C"
elif percentage >=55:
    grade = "C-"
else:
    grade = "F"
file.write('student name:')
file.write(student_name)
file.write('\n')
file.write('roll no:')
file.write(str(roll_no))
file.write('\n')
file.write('total number: ')
file.write(str(total))
file.write('\n')
file.write('percentage: ')
file.write(str(percentage))
file.write('\n')
file.write('grade: ')
file.write(str(grade))
file.write('\n')
file.close()
