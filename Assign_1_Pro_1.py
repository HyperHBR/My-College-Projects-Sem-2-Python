# Hardiksinh Rathod
# 21BCP128
# Program 1 Assignment-1

#Taking User Input

x = float(raw_input("Enter Float Number-1 = "))
y = float(raw_input("Enter Float Number-2 = "))

add = x + y  #Performing Addition
sub = x - y  #Performing Subtraction
mul = x * y  #Performing Multiplication
div = x / y  #Performing Division

#Printing Fractional Part Of Mathematical Operations

print(add.as_integer_ratio())
print(sub.as_integer_ratio())
print(mul.as_integer_ratio())
print(div.as_integer_ratio())


