num = int(input('Введите целое число: '))
ans = input('Перевести число в байты или киллобайты?')
if ans == 'b':
    print(f"{num} kb = {num * 1024} byte")
elif ans == 'k':
    print(f'{num} byte == {num / 1024} kb')
else:
    print("Wrong command")