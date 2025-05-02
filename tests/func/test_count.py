import pytest
from tasks import Task, count
import tasks


check_list = [
	([("Test", None, "down"), ("Test1", "Test2", True)], 2),
	([("Test", None, False)], 1),
	([], 0),
	(t:=[("Test", None, False) for i in range(1000)], len(t))
]

check_params = [f"Count tasks - {len(el[0])}, wait result - {el[1]}" for el in check_list]


@pytest.mark.parametrize("test, expected_result", check_list, ids=check_params)
def test_count(test, expected_result):
	for elem in test:
		tasks.add(Task(*elem))
	counter = count()
	assert counter == expected_result, \
	f"Wait {expected_result}, but result {counter}."
