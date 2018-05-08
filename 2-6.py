
first_set = set('aer1231231231823')
second_set = set('asd223')
print(first_set)

tuple1 = tuple(first_set & second_set, )
tuple2 = tuple(first_set - second_set,)

print(second_set)
print(tuple1[::-1])

list_of_tuples = list(tuple1) + list(tuple2)
print(list_of_tuples)

