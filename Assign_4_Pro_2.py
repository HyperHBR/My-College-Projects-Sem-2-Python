# Hardiksinh Rathod
# 21BCP128
# Program 1 Asssignment-4

# Defining The Functions
def sum(a,b):
    sum = a + b
    print("\nAdding {} with {} \n Ans = {}".format(a,b,sum))

def sub(a,b):
    sub = a - b
    print("\nSubtracting {} with {} \n Ans = {}".format(a,b,sub))

def mul(a,b):
    mul = a * b
    print("\nMultiplying {} with {} \n Ans = {}".format(a,b,mul))

def div(a,b):
    div = a / b
    print("\nDividing {} by {} \n Ans = {}".format(a,b,div))

# Taking User Input
a = int(input("Enter The Value Of a: "))
b = int(input("Enter The Value Of b: "))

#Calling Functions
sum(a,b)
sub(a,b)
mul(a,b)
div(a,b)