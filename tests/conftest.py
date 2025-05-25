# Памятка об интерфейсе Task constructor
# Task(summary=None, owner=None, done=False, id=None)
# summary то что требуется
# owner и done являются необязательными
# id задается базой данных
import pytest
import tasks
from tasks import Task


# # nothing here yet
# @pytest.fixture(autouse=True)
# def initialized_tasks_db(tmpdir):
#     """Connect to db before testing, disconnect after."""
#     # Setup : start db
#     tasks.start_tasks_db(str(tmpdir), "tiny")
#
#     yield # тут происходит тестирование
#
#     # Teardown : stop db
#     tasks.stop_tasks_db()


@pytest.fixture(scope="session")
def task_db_session(tmpdir_factory):
    """Create DB session"""
    temp_dir = tmpdir_factory.mktemp("temp")
    tasks.start_tasks_db(str(temp_dir), "tiny")
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def task_db(task_db_session):
    """An empty task db."""
    tasks.delete_all()


@pytest.fixture(scope="session")
def tasks_mult_per_owner():
    """Несколько владельцев с несколькими задачами каждый."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),
        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),
        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))


@pytest.fixture(scope="session")
def tasks_just_a_few():
    """Все резюме и владельцы уникальны."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture()
def db_with_3_tasks(task_db, tasks_just_a_few):
    for task in tasks_just_a_few:
        tasks.add(task)


@pytest.fixture()
def db_with_multi_per_owner(task_db, tasks_mult_per_owner):
    for task in tasks_mult_per_owner:
        tasks.add(task)
