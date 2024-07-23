'''
    15. Write a Python program to read a random line from a file.
'''
import random
a = open("abc.txt","r")
b = a.readlines()
c = random.choice(b)
print(c)
a.close()