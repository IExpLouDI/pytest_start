"""Placeholder."""
import pytest
import tasks


# nothing here yet
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield # тут происходит тестирование

    # Teardown : stop db
    tasks.stop_tasks_db()