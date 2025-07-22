from functools import reduce

str_numbers = list(map(str, [10, 20, 30, 40]))
print("Integers to strings:", str_numbers)

vowel_count = sum(1 for ch in "Hello World" if ch.lower() in "aeiou")
print("Vowel count in 'Hello World':", vowel_count)

reversed_words = ' '.join([word[::-1] for word in "Python is fun".split()])
print("Reversed words:", reversed_words)

factorial_5 = reduce(lambda x, y: x * y, range(1, 6))
print("Factorial of 5:", factorial_5)

unique_elements = list(dict.fromkeys([1, 2, 2, 3, 4, 4, 5]))
print("Unique elements:", unique_elements)

