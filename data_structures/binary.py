'''
Бинарный поиск чисел.
Для поиска массив (либо листы) должен быть отсортирован.
1. Берём ссылку на самое левое (нулевое) значение - start и правое (максимальное) значение - end.
2. Находим среднюю позицию через поиск длины массива и деления на два. - pos
3. Если загаданное число меньше среднего числа, то end берёт значение pos - 1, left сохраняет
своё значение, а pos берёт значение (end + start) // 2.
4. Если загаданное число меньше pos, то повторяем шаг 3.
Иначе, если з.число больше pos, то left = pos + 1, а end сохраняет свою позицию.
А затем обновляем значение pos = (left + right) // 2.
Если нашли, то отлично. Возвращаем ИНДЕКС найденного числа.
'''
import random


def bin_search(array, value):

	left = 0
	right = len(array) - 1
	pos = len(array) // 2

	while array[pos] != value and left <= right:
		if value > array[pos]:
			left = pos + 1
		else:
			right = pos - 1
		pos = (left + right) // 2

	return -1 if left > right else pos

tree = [x for x in range(100)]

tree.sort()
print(tree)

print(bin_search(tree, 111))