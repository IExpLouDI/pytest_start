import pytest


@pytest.fixture(name="lue")
def ultimate_answer_to_life_universe():
	"""Возвращает окончательный ответ"""
	return 42


def test_everything(lue):
	"""Использует более короткое имя"""
	assert lue == 42
