# Evklid's algorithm

def gcd(m, n):
	while m != n:
		if m > n:
			m -= n
		else:
			n -= m
	return m

def gcd2(m, n):
	if n == 0:
		return m
	return gcd2(n, m % 2)

def gcd3(m, n):
	while n != 0:
		m, n = n, m % n
	return m


print(gcd3(54, 241312313333332222))