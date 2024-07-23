# To count special character
a = open("abc.txt","r")
count=0
b = a.read()
for i in b:
    c = ord(i)
    if c>=0 and c<=47:
    # if i>='A' and i<='Z':
    #     pass
    # elif i>='a' and i<='z':
    #     pass
    # else:
        count+=1
print(count)
a.close()
# print(ord(" "))