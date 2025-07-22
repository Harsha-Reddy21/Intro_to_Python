# Traditional loop
squares_loop = []
for i in range(10):
    squares_loop.append(i * i)

# List comprehension
squares_lc = [i * i for i in range(10)]

# Output
print("1. Simple List Creation")
print("Traditional:", squares_loop)
print("List Comprehension:", squares_lc)
print()


# Traditional loop
evens_loop = []
for i in range(20):
    if i % 2 == 0:
        evens_loop.append(i)

evens_lc = [i for i in range(20) if i % 2 == 0]

# Output
print("2. With Filtering (Even Numbers)")
print("Traditional:", evens_loop)
print("List Comprehension:", evens_lc)
print()

# Traditional loop
pairs_loop = []
for x in [1, 2, 3]:
    for y in ['a', 'b']:
        pairs_loop.append((x, y))

# List comprehension
pairs_lc = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]

# Output
print("3. Nested Loops (Pairs)")
print("Traditional:", pairs_loop)
print("List Comprehension:", pairs_lc)
print()


matrix = [[1, 2], [3, 4], [5, 6]]

# Traditional loop
flattened_loop = []
for row in matrix:
    for item in row:
        flattened_loop.append(item)

# List comprehension
flattened_lc = [item for row in matrix for item in row]

# Output
print("4. Matrix Flattening")
print("Traditional:", flattened_loop)
