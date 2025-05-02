import tasks


def test_unique_id_1():
	"""unique_id должен возвращать неиспользуемый id."""
	ids = list()
	ids.append(tasks.add(tasks.Task("one")))
	ids.append(tasks.add(tasks.Task("two")))
	ids.append(tasks.add(tasks.Task("three")))
	# Захват уникального id
	uid = tasks.unique_id()
	# убеждаемся, что его нет в списке существующих идентификаторов
	assert uid in ids
