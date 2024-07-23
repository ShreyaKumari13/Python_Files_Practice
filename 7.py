'''
    7. Write a Python program to read a file line by line store it into an array.
'''
with open ("abc.txt", "r") as myfile:
    b = []
    for line in myfile:
        b.append(line)
    print(b)
