# No.of lines
a = open("abc.txt","r")
b = a.readlines()
c = len(b)
print("No.of lines: ",c)
a.close()
