import random
import math
int_seq = random.sample(range(100), 5)
float_random = random.random()
print(int_seq)
print(float_random)
int_seq_max = max(int_seq)
print(int_seq_max)
floor_div_result = int_seq_max // float_random
print(floor_div_result)
print(math.factorial(floor_div_result))
