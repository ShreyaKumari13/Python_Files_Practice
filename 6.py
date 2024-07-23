'''
    6. Write a Python program to read a file line by line store it into a variable.
'''
with open ("abc.txt", "r") as myfile:
    data = myfile.readlines()
    print(data)
