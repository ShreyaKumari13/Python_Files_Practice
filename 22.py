# To count number of characters
count = 0
a = open("abc.txt","r")
b = a.read()
for i in b:
    count+=1
print(count)
a.close()
