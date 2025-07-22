
def custom_map(func, iterable):
    return [func(item) for item in iterable]


def custom_filter(func, iterable):
    return [item for item in iterable if func(item)]

def custom_reduce(func, iterable):
    result=iterable[0]
    for item in iterable[1:]:
        result=func(result, item)
    return result



squared = custom_map(lambda x: x ** 2, [1, 2, 3, 4])
print("Squared:", squared)

evens = custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print("Evens:", evens)

total = custom_reduce(lambda x, y: x + y, [1, 2, 3, 4])
print("Sum:", total)

product = custom_reduce(lambda x, y: x * y, [1, 2, 3, 4])
print("Product:", product)

combined = custom_reduce(lambda x, y: x + y, ["Hi", " ", "there", "!"])
print("Combined String:", combined)
