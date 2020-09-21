import random

number = random.randint(0, 101)

while True:
	answer = (input("Write number"))
	if not answer or answer == "exit":
		break
	if not answer.isdigit():
		print("Write proper digit")
		continue
	user_answer = int(answer)

	if user_answer > number:
		print("Our number is less")
	elif user_answer < number:
		print("Out number is bigger")
	else:
		print("Congratulations, you guess it!")
		break