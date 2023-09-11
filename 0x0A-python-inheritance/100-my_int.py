#!/usr/bin/python3
"""a class MyInt that inherits from int"""

class MyInt(int):
    """a class MyInt that inherits from int"""
    
    def __eq__(self, value):
        """change opeartor"""
        return self.real != value

    def __ne__(self, value):
        """change opeartor"""
        return self.real == value
