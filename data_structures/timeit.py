#python3 -m timeit -n 100 -s "import alphabet_position"
# Сто попыток запустил код (модуль)
# import timeit
#
# x = 2 + 2
# print(timeit.timeit('x = 2 + 2'))

'''
Написали три функции, которые получают массив, находят сумму всех чисел и длину массива.
Через cProfile вызываем функцию, после чего видим итоги по времени работы каждой функции.
'''

import cProfile

def get_len(array):
	return len(array)

def get_sum(array):
	s = 0
	for i in array:
		s += i
	return s

def main():
	lst = [i for i in range(100)]
	a = get_len(lst)
	b = get_sum(lst)

cProfile.run('main()')