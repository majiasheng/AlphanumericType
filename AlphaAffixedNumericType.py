import re
class AlphaAffixedNumericType():
    '''
    Support arithmetic with different data types

    '''    
    def __init__(self, aant):
        assert aant.isalnum(), f'String "{aant}" is not alphanumeric'
        assert re.search("^[a-zA-Z]*\d*[a-zA-Z]*$", aant), f'String "{aant}" is not affixed'
        self.aant = aant

    def __add__(self, other):
        '''
        Increament numeric part of the type. 
        e.g. AlphanumericType("A130") + 1 = AlphanumericType("A131")
        :param other: whole number
        '''
        assert other.isdigit(), f'Operand "{other}" is not a valid number'
        other = int(other)

        


