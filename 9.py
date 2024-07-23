'''
    9. Write a Python program to count the number of lines in a text file.
'''
a = open("abc.txt","r")
lines = a.readlines()
line = len(lines)
print("No.of lines:",line)