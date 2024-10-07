import os
import pytest

from getdata import read_data

@pytest.fixture
def create_test_file():
    test_file= 'input.txt'
    with open(test_file, 'w') as f:
        f.write("test this test")
    yield test_file
    if os.path.exists(test_file):
        os.remove(test_file)

@pytest.fixture
def create_empty_file():
    emptyfile='empty.txt'
    with open(emptyfile, 'w') as f:
        pass
    yield emptyfile
    if os.path.exists(emptyfile):
        os.remove(emptyfile)


def test_read_file(create_test_file):
    content = read_data(create_test_file)
    assert content is not None

def test_empty_file(create_empty_file):
    content = read_data(create_empty_file)
    assert content == ""


