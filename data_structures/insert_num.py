import random

array = [random.randint(-5, 5) for _ in range(100)]

print(array)

num = int(input())
pos = int(input())

array.append(None)
i = len(array) - 1

while i > pos:
	array[i] = array[i - 1]
	array[i - 1] = array[i]
	i -= 1

array[pos] = num
print(array)
