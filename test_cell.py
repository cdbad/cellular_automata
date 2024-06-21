import pytest
from cell import CellClass

@pytest.mark.parametrize('rule', ['214',
                                  '110',
                                  '3',
                                  '255',
                                  '1',
                                  '0'])
def test_rule_length(rule):
    c = CellClass(rule, (40, 40))
    assert len(c.rule) == 8

# @pytest.mark.parametrize('rule', ['Hello',
#                                   'Poopoo',
#                                   (3, 4),
#                                   [2, 3, 4],
#                                   {'one': 1, 'two': 2},
#                                   -3])
# def test_rule_is_not_int_or_str(rule):
#     c = CellClass(rule, (40, 40))
#     if type(c.rule) == str:
#         with pytest.raises(ValueError):
#             assert int(c.rule)
#     elif type(c.rule) != int:
#         with pytest.raises(TypeError):
#             assert int(c.rule)

@pytest.mark.parametrize('rule', ['32',
                                  '200',
                                  34,
                                  '1',
                                  1000])
def test_rule_is__n_str_or_int(rule):
    c = CellClass(rule, (40, 40))
    if type(c.rule) == str:
        assert int(c.rule)
    elif type(c.rule) == int:
        assert c.rule > 0