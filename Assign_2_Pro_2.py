# Hardiksinh Rathod
# 21BCP128
# Program 2 Assignment-2

#Taking User Input

a = int(input("Enter Integer Number-1 = "))
b = int(input("Enter Integer Number-2 = "))
c = int(input("Enter Integer Number-3 = "))
d = int(input("Enter Integer Number-4 = "))
e = int(input("Enter Integer Number-5 = "))

#Getting Maximum Of Entered Value And Assigning It To maximum Variable
maximum = max(a,b,c,d,e)
print("\nThe Maximum Value From The Entered Value = {}".format(maximum))

#Getting Minimum Of Entered Value And Assigning It To minimum Variable
minimum = min(a,b,c,d,e)
print("The Minimum Value From The Entered Value = {}".format(minimum))

#Getting Quotient When Max Is Divided By Min And Assigning It To quo Variable
quo = maximum / minimum
print("\nThe Value Of Quotient When Maximum Is Divided By Minimum  = {}".format(quo))

#Getting Remainder When Max Is Divided By Min And Assigning It To rem Variable
rem = maximum % minimum
print("The Value Of Remainder When Maximum Is Divided By Minimum  = {}".format(rem))