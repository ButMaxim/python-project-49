from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
	first_num, second_num = randint(1, 100), randint(1, 100)
	correct_answer = str(computeGCD(first_num, second_num))
	task = f'{first_num} {second_num}'
	return correct_answer, task


def computeGCD(x, y):
	if x > y:
		small = y
	else:
		small = x
	for i in range(1, small + 1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i
	return gcd
