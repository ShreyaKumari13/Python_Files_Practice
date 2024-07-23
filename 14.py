'''
    14. Write a Python program to combine each line from first file with the corresponding line in second file.
'''
a = open("abc.txt","r")
b = open("test.txt","r")
for i,j in zip(a,b):
    print(i+j,end="")
a.close()
b.close()