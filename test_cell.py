import pytest
from cell import CellClass

@pytest.mark.parametrize('input', ['214',
                                  '110',
                                  '3'])
def test_rule_length(input):
    c = CellClass(input)
    assert len(c.rule) == 8