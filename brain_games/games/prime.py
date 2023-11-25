from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(task):
	i = 2
	while i <= sqrt(task):
		if task % i == 0:
			correct_answer = 'no'
			return correct_answer
		else:
			i += 1
			correct_answer = 'yes'
	return correct_answer

def make_question():
	task = randint(0,100)
	correct_answer = is_prime(task)
	return correct_answer, task

