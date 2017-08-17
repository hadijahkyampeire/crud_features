""" creating a list"""
myList = {"A":"Apple", "B":"Bread", "C":"Carrots"}

""" read/assess items in a list"""
>>> myList["A"]
'Apple'
>>> myList["B"]
'Bread'
>>> myList["C"]
'Carrot'

""" updating a list"""

>>> myList["B"] = "Banana"
>>> myList["B"]
'Banana'
>>> myList
{'A': 'Apple', 'C': 'Carrots', 'B': 'Banana'}
"""deleting items"""
>>> myList
{'A': 'Apple', 'C': 'Carrots', 'B': 'Banana'}
>>> del myDict["A"]
>>> myList
{'C': 'Carrot', 'B': 'Banana'}
""" if you want to delete all items"""
>>> myList
{'C': 'Carrot', 'B': 'Banana'}
>>> myList.clear()
>>> myList
{}