from collections import namedtuple


"""Проверка типа данных"""
task = namedtuple("Task", ["summary", "owner","done", "id"])
task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
	print("Hello")
	"""Использование параметров не должно вызывать значения по умолчанию"""
	t1 = task()
	t2 = task(None, None, False, None)
	assert t1 == t2

def test_member_access():
	"""Проверка свойсват .field (поля) namedtuple"""
	t = task("buy milk", "brian")
	assert t.summary == "buy milk"
	assert t.owner == "brian"
	assert (t.done, t.id) == (False, None)

