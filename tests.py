from AlphaAffixedNumericType import AlphaAffixedNumericType

def test_add_0_equal():
    v1 = AlphaAffixedNumericType('A123')
    expected = AlphaAffixedNumericType('A123').get_value()
    actual = (v1 + 0).get_value()
    assert actual == expected, f'actual: {actual}, expected: {expected}'
    print('Passed test_add_0_equal')

def test_add_1_equal():
    v1 = AlphaAffixedNumericType('A123')
    expected = AlphaAffixedNumericType('A124').get_value()
    actual = (v1 + 1).get_value()
    assert actual == expected, f'actual: {actual}, expected: {expected}'
    print('Passed test_add_1_equal')

def test_add_1000_equal():
    v1 = AlphaAffixedNumericType('A123')
    expected = AlphaAffixedNumericType('A1123').get_value()
    actual = (v1 + 1000).get_value()
    assert actual == expected, f'actual: {actual}, expected: {expected}'
    print('Passed test_add_1000_equal')

def test_minus_1_equal():
    v1 = AlphaAffixedNumericType('A123')
    expected = AlphaAffixedNumericType('A122').get_value()
    actual = (v1 - 1 ).get_value()
    assert actual == expected, f'actual: {actual}, expected: {expected}'
    print('Passed test_minus_1_equal')

def test_minus_self_is_0():
    v1 = AlphaAffixedNumericType('A123')
    expected = 0
    actual = v1 - v1
    assert actual == expected, f'actual: {actual}, expected: {expected}'
    print('Passed test_minus_self_is_0')

def test_minus_1_less_than_self_is_1():
    v1 = AlphaAffixedNumericType('A123')
    expected = 1
    actual = v1 - AlphaAffixedNumericType('A122')
    assert actual == expected, f'actual: {actual}, expected: {expected}'
    print('Passed test_minus_1_less_than_self_is_1')

test_add_0_equal()
test_add_1_equal()
test_add_1000_equal()
test_minus_1_equal()
test_minus_self_is_0()
test_minus_1_less_than_self_is_1()