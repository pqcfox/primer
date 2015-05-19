import pytest

@pytest.fixture(scope="module")
def less_than_two():
    return [-512, -283, -7/6, -0.23, 0, 0.2, 1, 1.3]
