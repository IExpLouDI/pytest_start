from collections import namedtuple
import pytest


"""Проверка типа данных"""
task = namedtuple("Task", ["summary", "owner", "done", "id"])
task.__new__.__defaults__ = (None, None, False, None)


@pytest.mark.run_these_please
def test_asdict():
	"""_asdict должен возвращать словарь."""
	t_task = task("test 1", "test 2", True, 22)
	t_dict = t_task._asdict()
	expected = {"summary": "test 1",
				"owner": "test 2",
				"done": True,
				"id": 22}
	assert t_dict == expected


def test_replace():
	"""Должно изменить переданное в fields."""
	t_before = task("start 1", "second 2", False)
	t_after = t_before._replace(id=10, done=True)
	t_expected = task("start 1", "second 2", True, 10)
	assert t_after == t_expected
