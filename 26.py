# To count occurence of a word
a = open("abc.txt","r")
b = a.read()
c = b.split()
count = 0
for i in c:
    if i=="the":
        count+=1
print(count)
a.close()