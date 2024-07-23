'''
    12. Write a Python program to write a list to a file.
'''
list1 = ["I am Shreya",'Kumari','Singh']
a = open("abc.txt","a")
for i in list1:
    a.write(i+"\n")
a.close()