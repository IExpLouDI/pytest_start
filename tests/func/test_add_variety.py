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

"""
Упражнения
1. Загрузите проект для этой главы, task_proj, с веб-страницы этой главы и убедитесь, что вы можете установить его локально с помощь
install /path/to/tasks_proj.
2. Изучите каталог тестов.
3. Запустите pytest с одним файлом.
4. Запускать pytest против одного каталога, например tasks_proj/tests/func. Используйте pytest для запуска тестов по отдельности, а та
полный каталог одновременно. Там есть несколько неудачных тестов. Вы понимаете, почему они терпят неудачу?
5. Добавляйте xfail или пропускайте маркеры к ошибочным тестам, пока не сможете запустить pytest из каталога tests без аргументов и ош
6. У нас нет тестов для tasks.count(), среди прочих функций. Выберите непроверенную функцию API и подумайте, какие тестовые случа
нужны, чтобы убедиться, что она работает правильно.
7. Что произойдет при попытке добавить задачу с уже установленным идентификатором? Есть некоторые отсутствующие тесты исключен
test_api_exceptions.py. Посмотрите, можете ли вы заполнить недостающие исключения. (Это нормально посмотреть api.py для этог
упражнения.)
"""
