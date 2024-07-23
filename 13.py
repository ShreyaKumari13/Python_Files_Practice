'''
    13. Write a Python program to copy the contents of a file to another file .
'''
# a = open("abc.txt","r")
# b = a.read()
# c = open("copy.txt","a")
# c.write(b)
# a.close()
# c.close()

from shutil import copyfile
copyfile('abc.txt','test.txt')

