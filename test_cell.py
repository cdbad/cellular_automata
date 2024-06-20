import pytest
from cell import CellClass

@pytest.mark.parametrize('input', ['214',
                                  '110',
                                  '3',
                                  '255',
                                  '1',
                                  '0'])
def test_rule_length(input):
    c = CellClass(input, (40, 40))
    assert len(c.rule) == 8

# @pytest.mark.parametrize('width')