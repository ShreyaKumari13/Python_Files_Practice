'''
    2. Write a Python program to read first n lines of a file.
'''
f = open("abc.txt","r")
line = int(input("Enter the no.of lines to be read: "))
for i in range(line):
    a = f.readline()
    print(a,end="")
f.close()