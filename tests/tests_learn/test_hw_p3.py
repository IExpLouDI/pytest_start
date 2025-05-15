import random

import pytest


# 1. Создать тестовый файл
# 2.Напишите несколько fixtures—functions данных с помощью
# декоратора @pytest.fixture(), которые будут возвращать некоторые данные
# Возможно, список или словарь, или кортеж.
# 2. Для каждой фикстуры напишите хотя бы одну тестовую функцию, которая её использует.
# 3. Напишите два теста, которые используют одну и ту же фикстуру.
# 4. Запустить pytest --setup-show test_fixtures.py. Все фикстуры работают перед каждым тестом?
# 5. Добавьте scope= 'module' в фикстуру из упражнения 4.
# 6. Повторно запустите pytest --setup-show test_fixtures.py. Что изменилось?
# 7. Для фикстуры из упражнения 6 измените return <data> на yield <data>.
# 8. Добавить операторы печати до и после yield.
# 9. Запустите pytest -s -v test_fixtures.py. Имеет ли результат смысл?

#2
gen_list = [random.randint(0, 1000) for i in range(10)]


def generate_ids(fixture_value):
	return f"This's {fixture_value}"

@pytest.fixture(params=gen_list, ids=generate_ids)
def generate_data(request):
	yield request.param

def test_my_fixture(generate_data):
	t = random.randint(0, 1000)
	assert t * 2 > generate_data * 2