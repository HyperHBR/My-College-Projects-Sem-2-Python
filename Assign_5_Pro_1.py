# Hardiksinh Rathod
# 21BCP128
# Program 1 Assignment-5
# Zero Division Error Program

# Taking User Input
dividend = float(input("Enter The Value Of Dividend: "))
divisor = float(input("Enter The Value Of Divisor: "))

# Error Handling
try:
    ans = dividend/divisor
    print(ans)
except:
    print("Error Occured = Zero Division Error")