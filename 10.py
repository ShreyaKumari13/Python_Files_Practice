'''
    10. Write a Python program to count the frequency of words in a file.
'''
count = 0
a = open("abc.txt","r")
# count = 0
for lines in a:
    b = lines.split()
    for word in b:
        if word=="the":
             count+=1
print(count)
a.close()
