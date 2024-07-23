'''
    5. Write a Python program to read a file line by line and store it into a list.
'''
a = open("abc.txt","r")
c = a.readlines()
print(c)
a.close()