import pytest

@pytest.mark.parametrize('num', range(10))
def test_even_number(num):
    assert num % 2 == 0

if __name__ == '__main__':
    pytest.main(['-v', '-s', '--pdb'])