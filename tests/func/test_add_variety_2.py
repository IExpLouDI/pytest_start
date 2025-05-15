from pickle import FALSE

import pytest
import tasks
from tasks import Task


task_to_try = (
	Task("sleep", done=True),
	Task("wake", "brian"),
	Task("breathe", "BRIAN", True),
	Task("exercise", "BrIaN", False)
)

task_ids = [f"Task({t.summary}, {t.owner}, {t.done}" for t in task_to_try]


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


@pytest.mark.parametrize("task",
						 [Task("sleep", done=True),
						  Task("wake", "brian"),
						  Task("breathe", "BRIAN", True),
						  Task("exercise", "BrIaN", False)])
def test_add_2(task):
	"""tasks.get использует id, возвращаемый из add works."""
	task_id = tasks.add(task)
	t_from_db = tasks.get(task_id)
	# всё, кроме идентификатора, должно быть одинаковым
	assert equivalent(t_from_db, task)


@pytest.mark.parametrize("summary, owner, done",
						 [("sleep", None, False),
						  ("wake", "brian", False),
						  ("breathe", "BRIAN", True),
						  ("eat eggs", "BrIaN", False)])
def test_add_3(summary, owner, done):
	"""tasks.get использует id, возвращаемый из add works."""
	task = Task(summary, owner, done)
	task_id = tasks.add(task)
	t_from_db = tasks.get(task_id)
	# всё, кроме идентификатора, должно быть одинаковым
	assert equivalent(t_from_db, task)


@pytest.mark.parametrize("task", task_to_try)
def test_add_4(task):
	"""tasks.get использует id, возвращаемый из add works."""
	task_id = tasks.add(task)
	t_from_db = tasks.get(task_id)
	# всё, кроме идентификатора, должно быть одинаковым
	assert equivalent(t_from_db, task)


# Указываем созданные айдишники, для удобства чтения тестов
@pytest.mark.parametrize("task", task_to_try, ids=task_ids)
def test_add_5(task):
	"""tasks.get использует id, возвращаемый из add works."""
	task_id = tasks.add(task)
	t_from_db = tasks.get(task_id)
	# всё, кроме идентификатора, должно быть одинаковым
	assert equivalent(t_from_db, task)


@pytest.mark.parametrize("task", task_to_try, ids=task_ids)
class TestAdd:
	"""Демонстрация параметризации тестовых классов"""

	def test_equivalent(self, task):
		task_id = tasks.add(task)
		t_from_db = tasks.get(task_id)
		assert equivalent(t_from_db, task)


	def test_valid_id(self, task):
		"""Мы можем использовать одни и теже данные или несколько тестов."""
		task_id = tasks.add(task)
		t_from_db = tasks.get(task_id)
		assert t_from_db.id == task_id


@pytest.fixture(params=task_to_try)
def a_task(request):
	return request.param


@pytest.fixture(params=task_to_try, ids=task_ids)
def b_task(request):
	return request.param


def test_add_a(task_db, a_task):
	task_id = tasks.add(a_task)
	t_from_db = tasks.get(task_id)
	assert equivalent(t_from_db, a_task)


def test_add_b(task_db, b_task):
	task_id = tasks.add(b_task)
	t_from_db = tasks.get(task_id)
	assert equivalent(t_from_db, b_task)


def id_func(fixture_value):
	"""Функция генерации идентификатора фикстуры"""
	t = fixture_value
	return f"Task({t.summary}, {t.owner},{t.done})"


@pytest.fixture(params=task_to_try, ids=id_func)
def c_task(request):
	return request.param


def test_add_c(task_db, c_task):
	task_id = tasks.add(c_task)
	t_from_db = tasks.get(task_id)
	assert equivalent(t_from_db, c_task)
