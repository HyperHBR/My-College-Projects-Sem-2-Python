# Hardiksinh Rathod
# 21BCP128
# Program 2 Assignment-5
# File Error Program

# Error Handling
try:
    f = open("Test.txt", "r")
    data = f.read()
    print(data)

except:
    print("Error Occured = File Handling Error {}".format(IOError))

else:
    f.close()
    print("Task Completed")
