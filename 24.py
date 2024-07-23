# To count no.of lowercase
count = 0
a = open("abc.txt","r")
b = a.read()
for i in b:
    if i>="a" and i<="z":
        count+=1
print(count)
a.close() 