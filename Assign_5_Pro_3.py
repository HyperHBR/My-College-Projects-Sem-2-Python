# Hardiksinh Rathod
# 21BCP128
# Program 3 Assignment-5
# Value Error Program

# Importing
from math import sqrt

# Error Handling
x = int(input("Enter The Number = "))

try:
    print("Square Root Of {} = {}".format(x,sqrt(x)))

except:
    print("Error Occured = Value Error")
    print("Square Root Of Negative Number Is Only Possible In Complex Domain")