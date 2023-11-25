from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
	first_num, second_num = randint(1, 100), randint(1, 100)
	correct_answer = str(gcd(first_num, second_num))
	task = f'{first_num} {second_num}'
	return correct_answer, task
