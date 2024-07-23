'''
    8. Write a python program to find the longest words.
'''
a = open("abc.txt","r")
c = a.read()
b = c.split()
max1 = ''
for i in b:
    if len(i) > len(max1):
        max1 = i
print(max1)
a.close