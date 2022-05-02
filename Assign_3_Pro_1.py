# Hardiksinh Rathod
# 21BCP128
# Program 1 Assignment-3

#Taking User Input
x = int(raw_input("Enter Integer Number= "))
count = 1 #Setting Up Count

print("\n-------The Multiplication Table Of {}-------".format(x))

#Using While Loop
while count<=10:
    print("{} X {} = {}".format(x, count, x*count))
    count += 1
