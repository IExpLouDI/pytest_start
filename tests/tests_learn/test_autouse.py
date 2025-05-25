import pytest
import time


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
	"""Сообщает время в конце сессии."""
	yield
	now = time.time()
	print("-" * 20)
	print(f"Finished: {time.strftime('%d %b %x', time.localtime(now))}")


@pytest.fixture(autouse=True)
def footer_function_scope():
	"""Сообщает продолжительность теста после каждой функции"""
	start = time.time()
	yield
	stop = time.time()
	delta = stop - start
	print("-" * 20)
	print(f"Test duration: {delta:0.3} seconds.")


def test_1():
	"""Имитирует длительный тест"""
	time.sleep(1)


def test_2():
	"""Имитирует более длинный тест"""
	time.sleep(1.5)
