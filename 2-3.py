import string
x = string.ascii_lowercase + string.ascii_uppercase + string.digits
print(x)
print(x[0])
print(x[-1])
print(x[2])
print(x[-3])
print(x[:8])
print(x[::3])
print(x[len(x)//2:len(x)//2+1])
print(x[::-1])
