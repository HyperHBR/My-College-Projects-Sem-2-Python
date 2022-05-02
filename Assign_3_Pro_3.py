# Hardiksinh Rathod
# 21BCP128
# Program 3 Assignment-3

#Setting Up sum = 0 And num Value To 1
sum = 0
num = 1

#Using While Loop To Loop From 1 To 100
while num<=100:
    if num%2==0 or num%3==0: #Checking Whether Current num Is Divisble By 2 Or 3
        sum += num #If Num Is Divisible By 2 Or 3 Then Adding It To sum
    num += 1 #Incrementing num

#Printing sum
print("\nThe Sum Of Numbers From 1 To 100 Divisible By 2 Or 3 = {}\n".format(sum))