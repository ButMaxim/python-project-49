from random import randint
import prompt


def main():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello, ' + name + '!')
	i = 0
	while i < 3:
		num = randint(0, 100)
		print('Question: ' + str(num))
		user_answer = prompt.string('Your answer: ')
		if num % 2 == 0:
			correct_answer = "yes"
	
		else:
			num % 2 != 0
			correct_answer = "no"

		if user_answer == correct_answer:
			print("Correct!")
			i += 1

		else:
			print(f'{user_answer}, is wrong answer ;(. Correct answer was {correct_answer}')
			print("Let's try again, " + name + "!")
			break
