
from functools import reduce

factorial = lambda n: reduce(lambda a, b: a * b, range(1, n + 1))
print(factorial(5))  


