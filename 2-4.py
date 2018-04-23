import string
x = string.ascii_lowercase + string.ascii_uppercase + string.digits
x = list(x)

print(x)
print([c for c in x if "0" <= c <= "9"])
new_str1 = "".join(x)
new_str2 = str(x)
print(new_str1, type(new_str1))
print(new_str2, type(new_str2))
print(new_str1[0])
print(new_str2[0])