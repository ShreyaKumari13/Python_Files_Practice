# To print No.of words
a = open("abc.txt","r")
b = a.read()
c = b.split()
count = 0
for i in c:
    count+=1
print(count)
a.close()