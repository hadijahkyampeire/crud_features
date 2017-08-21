import unittest 
from shoppinglist import shoppinglist
from shoppinglist import item

class shoppinglistTestCase(unittest.TestCase):
    """docstring for Testshoppinglist"""
    def setUp(self):
        self.listCreated = shoppinglist() 
    
    