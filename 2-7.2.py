
myfile = open('C:\\myfile.txt', 'r+')
print(myfile.read())

myfile.seek(len("Hello "))
myfile.write("MY  " + "fiLe world!")
myfile.flush()

