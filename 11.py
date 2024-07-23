'''
    11. Write a Python program to get the file size of a plain file.
'''
a = open("abc.txt","r")
b = a.read()
c = len(b)
print("The size of the file is:",c)
a.close()