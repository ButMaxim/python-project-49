from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
	task = randint(1, 100)
	correct_answer = is_even(task)
	return correct_answer, task

def is_even(task):
    return 'yes' if task % 2 == 0 else 'no'
