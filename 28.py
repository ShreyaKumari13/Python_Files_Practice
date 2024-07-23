# size of bytes
count = 0
a = open("abc.txt","r")
b = a.read()
for i in b:
    count+=1
print("Total number of bytes:",count)
a.close()
