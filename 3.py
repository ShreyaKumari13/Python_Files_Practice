'''
    3. Write a Python program to append text to a file and display the text.
'''
a = open("abc.txt","a")
a.write("So live it the way you like it.")
a.close()
b = open("abc.txt","r")
print(b.readlines())
b.close()

