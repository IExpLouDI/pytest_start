import random

import pytest


@pytest.mark.run_these_please
def test_art():
	a = random.randint(0,100)
	b = random.randint(1, 5)
	assert a > b
