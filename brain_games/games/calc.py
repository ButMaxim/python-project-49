from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'
operators = {
		'+': add,
		'-': sub,
		'*': mul
	}

def make_question():
	first_num, second_num = randint(1, 100), randint(1, 100)
	operator = choice(list(operators.keys()))
	correct_answer = str(operators[operator](first_num, second_num))
	task = f'{first_num} {operator} {second_num}'
	return correct_answer, task
	
