"""Проверяем функцию API tasks.add"""

import pytest
import tasks
from tasks import Task


def test_add():
    """Placeholder test."""
    pass


def test_add_returns_valid_id():
    """tasks.add(valid_task) должен возвращать целое число"""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Убедимся, что поле task_id установлено tasks.add()."""
    # GIVEN an initialized tasks db
    # AND a new task is added
    new_task = Task("sit in chair", owner="me", done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.add(new_task)

    # WHEN task is retieved
    task_from_db = tasks.get(task_id)

    # WHEN task_id matches id field
    assert task_from_db.id == task_id


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield # тут происходит тестирование

    # Teardown : stop db
    tasks.stop_tasks_db()
