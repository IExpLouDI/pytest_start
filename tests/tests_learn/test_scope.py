import pytest


@pytest.mark.usefixtures("class_scope")
class TestSomething:
	"""Demo class scope fixtures"""

	def test_3(self):
		"""Test using a scope fixtures."""

	def test_4(self):
		"""Again, multiply test are more fun"""
