'''
    4. Write a Python program to read last n lines of a file.
'''
a = open("abc.txt","r")
lines = a.readlines()
n = int(input("Enter the no.pf last lines required: "))
last_lines = lines[-n:]
print(last_lines)