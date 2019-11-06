import re

class AlphaAffixedNumericType(): # 'aant' for short
'''
Support arithmetic with different data types
'''
ALPHA_AFFIXED_NUMERIC_TYPE_REGEX = r"^([a-zA-Z])(\d+)([a-zA-Z])$"
INDEX_OF_PREFIX_GROUP = 0
INDEX_OF_NUMBER_GROUP = 1
INDEX_OF_POSTFIX_GROUP = 2

def __init__(self, aant):
    self.mo = re.match(AlphaAffixedNumericType.ALPHA_AFFIXED_NUMERIC_TYPE_REGEX, aant)
    assert aant.isalnum(), f'String "{aant}" is not alphanumeric'
    assert self.mo, f'String "{aant}" is not affixed'
    self.aant = aant

def get_prefix_part_of_aant(self):
    return self.mo.groups()[AlphaAffixedNumericType.INDEX_OF_PREFIX_GROUP]

def get_numeric_part_of_aant(self):
    return self.mo.groups()[AlphaAffixedNumericType.INDEX_OF_NUMBER_GROUP]

def get_postfix_part_of_aant(self):
    return self.mo.groups()[AlphaAffixedNumericType.INDEX_OF_POSTFIX_GROUP]

@staticmethod
def add_int_list(int_list_1, int_list_2):
    l1 = len(int_list_1)
    l2 = len(int_list_2)
    if l2 > l1:
        int_list_1 = [0] * (l2 - l1) + int_list_1
    elif l1 > l2:
        int_list_2 = [0] * (l1 - l2) + int_list_2

    carry, n1, n2 = 0, 0, 0

    for i in range(len(int_list_1) - 1, -1 , -1):
        n1 = int_list_1[i]
        n2 = int_list_2[i]
        s = n1 + n2 + carry
        carry = s // 10
        int_list_1[i] = s % 10
    
    if carry > 0:
        int_list_1 = [carry] + int_list_1
    
    return int_list_1

def __add__(self, other):
    '''
    Increament numeric part of the type. 
    e.g. AlphanumericType("A130") + 1 = AlphanumericType("A131")
    :param other: whole number
    '''
    assert str(other).isdigit(), f'Operand "{other}" is not a valid number'
    other = [int(d) for d in str(other)]

    numeric_part_of_aant = self.get_numeric_part_of_aant()
    numeric_part_of_aant = [int(d) for d in str(numeric_part_of_aant)]

    new_numeric_part_of_aant = ''.join(
        [
            str(i) for i in AlphaAffixedNumericType.add_int_list(
                            other,
                            numeric_part_of_aant
                        )
        ]
    )

    return AlphaAffixedNumericType(
        self.get_prefix_part_of_aant() + \
        new_numeric_part_of_aant + \
        self.get_postfix_part_of_aant()
    )

def __repr__(self):
    return self.aant
