import pytest
import tasks


@pytest.mark.xfail(tasks.__version__ < "0.2.0",
                   reason="not supported until version 0.2.0")
def test_unique_id():
    """Вызов unique_id дважды должен возвращать разные числа."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Демострация xfail."""
    uid = tasks.unique_id()
    assert uid == "a duck"


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Демострация xpass."""
    uid = tasks.unique_id()
    assert uid != "a duck"



def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = list()
    ids.append(tasks.add(tasks.Task('one')))
    ids.append(tasks.add(tasks.Task('two')))
    ids.append(tasks.add(tasks.Task('three')))
    # grab a unique id
    uid = tasks.unique_id()
    # make sure it isn't in the list of existing ids
    assert uid not in ids
