'''
    17. Write a Python program to remove newline characters from a file.
'''
a = open("abc.txt","r")
b = a.readlines()
c = []
for i in b:
    d = i.rstrip("\n")
    c.append(d)
print(c)
a.close()
