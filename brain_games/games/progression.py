from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
	first_num = randint(1, 100)
	progression_step = randint(1, 10)
	task = []
	for i in range(10):
		first_num += progression_step
		task.append(first_num)

	rand_index = randint(0, 9)
	correct_answer = str(task[rand_index])
	return task, correct_answer, rand_index


def make_question():
	task, correct_answer, rand_index = make_progression()
	task[rand_index] = '..'
	task = ' '.join(str(i) for i in task)
	return correct_answer, task
