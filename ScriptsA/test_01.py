import pytest

def test_a():
    print("---->test_a")
    assert 2>1

def test_b():
    print("---->test_b")
    assert  False

if __name__ == '__main__':
    pytest.main(["test_01.py"])
