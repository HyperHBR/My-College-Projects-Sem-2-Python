# Hardiksinh Rathod
# 21BCP128
# Program 2 Assignment-6
# Dictionary Problem

# Defining An Empty Dictionary
admissions = {}
current_student_number = 1

print("\n--------Taking Details Of 10 Students--------")

while current_student_number <= 10: # Running A Loop
    
    add_no = input("\nPlease Enter The Admission Number = ") #Asking For Number
    name = raw_input("Please Enter The Student's Name = ") #Asking For Name
    admissions[add_no] = name # Assigning name Value To add_no Key

    if current_student_number == 10:
        break

    current_student_number += 1

# Printing Dictionary Directly
print(admissions)

# Printing Each Number And Name Of Student Separately
print("\n**********Printing Each Student's Detail:**********")
for number,adm in admissions.items():
    print("-->Admission number Of {} Is {}".format(adm,number))

