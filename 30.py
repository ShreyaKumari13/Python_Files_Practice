# first word
a = open("abc.txt","r")
for i in a:
    words = i.split()
    print(words[0])
a.close()
