# Hardiksinh Rathod
# 21BCP128
# Program 1 Assignment-2

#Taking User Input

x = float(input("Enter Float Number-1 = "))
y = float(input("Enter Float Number-2 = "))

print("\n*************The Two Values You Entered Are*************\n")
print("First(x) = {}".format(x))
print("Second(y) = {}".format(y))

print("\n*************Performing Arithmetic Operations*************\n")

print("At The Start Of Current Opertaion\nx = {}\ny = {}\n".format(x,y))
print("x + y = {}".format(x+y)) # Addition(+)
print("x - y = {}".format(x-y)) # Subtraction(-)
print("x * y = {}".format(x*y)) # Multiplication(*)
print("x / y = {}".format(x/y)) # Division(/)
print("x % y = {}".format(x%y)) # Modulus(%)
print("x to the power y = {}".format(x**y)) # Exponentiation(**)
print("x // y = {}".format(x//y)) # Floor Divison(//)

print("\n*************Performing Assignment Operations*************\n")

print("At The Start Of Current Opertaion\nx = {}\ny = {}\n".format(x,y))
#Assigning Value Of x equal to y (=)
x = y 
print("x is assigned value ={}".format(y))
#Incrementing Current Value Of x By y unit (+=)
x += y 
print("x+=y --> {}".format(x))
#Decrementing Current Value Of x By y units
x -= y 
print("x-=y --> {}".format(x))
#Multiplying Current Value Of x By y
x *= y
print("x*=y --> {}".format(x))
#Dividing Current Value Of x By y
x /= y 
print("x/=y --> {}".format(x))
#Assigning x The Value Equal x to the power y
x **= y 
print("x**y --> {}".format(x))
#Assigning x The Value Equal x // y
x //= y 
print("x//=y --> {}".format(x))
#Assigning x The Value Equal To The Remainder When x Is Divided By y
x %= y 
print("x%=y --> {}".format(x))

print("\n*************Performing Comparision Operations*************\n")

print("At The Start Of Current Opertaion\nx = {}\ny = {}\n".format(x,y))
#Checking Whether x And y Are Equal
print("Is x equal y ? --> {}".format(x==y))  
#Checking Whether x And y Are Not Equal
print("Is x not equal y ? --> {}".format(x!=y)) 
#Checking Whether x Is Greater Than y
print("Is x greater than y ? --> {}".format(x>y)) 
#Checking Whether x Is Lesser Than y
print("Is x lesser than y ? --> {}".format(x<y)) 
#Checking Whether x Is Greater Than Or Equal To y
print("Is x greater than or equal to y ? --> {}".format(x>=y)) 
#Checking Whether x Is Lesser Than Or Equal To y
print("Is x lesser than or equal to y ? --> {}".format(x<=y)) 

print("\n*************Performing Logical Operations*************\n")

print("At The Start Of Current Opertaion\nx = {}\ny = {}\n".format(x,y))
#Checking Whether x And y Both Are Less Than 10 Or Not -- and Operator
print("Is x<10 and y<10 --> {}".format(x<10 and y<10))
#Checking Whether x Or y Is/Are Greater Than 2 Or Not -- or Operator
print("Is x>2 or y>2 --> {}".format(x>2 or y>2))
#Reversing The Result Using Not Statement -- not Operator
print("Is y>10 --> {}".format(not(x>10)))

print("\n*************Performing Identity Operations*************\n")

print("At The Start Of Current Opertaion\nx = {}\ny = {}\n".format(x,y))
#Checking Whether x And y Are Same Or Not -- is Operator
print("Are x and y same> --> {}".format(x is y))

#Checking Whether x And y Are Same Or Not -- is not Operator
print("Are x and y not same> --> {}".format(x is not y))









