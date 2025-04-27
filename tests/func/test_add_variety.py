import pytest
import tasks
from tasks import Task


def test_add_1():
	"""tasks.get использует id, возвращаемый из add works."""
	task = Task("breathe", "BRIAN", True)
	task_id = tasks.add(task)
	t_from_db = tasks.get(task_id)
	# всё, кроме идентификатора, должно быть одинаковым
	assert equivalent(t_from_db, task)

def equivalent(t1, t2):
	"""Проверяем эквивалентность двух задач"""
	# Сравнить всё, кроме поля id
	return ((t1.summary == t2.summary) and
			(t1.owner == t2.owner) and
			(t1.done == t2.done))
