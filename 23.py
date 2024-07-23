# To count no.of uppercase
count = 0
a = open("abc.txt","r")
b = a.read()
for i in b:
    if i>="A" and i<="Z":
        count+=1
print(count)
a.close() 