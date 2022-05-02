# Hardiksinh Rathod
# 21BCP128
# Program 4 Assignment-3

#Taking Float As User Input
x = float(raw_input("Enter Side Of Square(float): "))

#Using While Loop
while x:
    if (x>0): #Checking Whether Number Is Positive Or Not
        print("\nThe Area Of Square = {}.".format(x*x)) #Printing Area
        break
    else:
        print("\nPlease Enter A Postive Value Only") #Asking To Re-input
        x = float(raw_input("Enter Side Of Square(float): "))
        continue #Going Back To The Beginning Of The Loop
