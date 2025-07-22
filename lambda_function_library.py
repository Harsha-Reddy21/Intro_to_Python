from functools import reduce


square = lambda x: x * x
print("Square of 5:", square(5))


factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else 1
print("Factorial of 5:", factorial(5))


reverse_string = lambda s: s[::-1]
print("Reverse:", reverse_string("hello"))


to_upper = lambda s: s.upper()
print("Uppercase:", to_upper("lambda"))



filter_evens = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
print("Even numbers in [1, 2, 3, 4, 5]:", filter_evens([1, 2, 3, 4, 5]))



sum_list = lambda lst: sum(lst)
print("Sum of [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))
