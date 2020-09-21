def binary(num):
	string = ""
	while num > 0:
		string = f'{num % 2}{string}'
		num //= 2
	return string

# print(binary(255))

while True:
	n = int(input())
	if n != 0:
		print(binary(n))
	else:
		break