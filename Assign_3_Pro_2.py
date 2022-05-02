# Hardiksinh Rathod
# 21BCP128
# Program 2 Assignment-3

#Setting Up Count And Number Of Vowel
count = 1
vowel = 0

#Using While Loop
while count<= 10:
    ch = raw_input("Enter Character: ") # Taking Input

    if(    ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U"
        or ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"): #Checking ch
        vowel += 1 #Incrementing Vowel

    count += 1 #Incrementing Count

print("\nTotal Vowels Entered = {}.".format(vowel))