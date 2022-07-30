import unittest

from translator import english_to_french, french_to_english

class TestEn2Fr(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(english_to_french(""),)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
        self.assertEqual(english_to_french("Thank you"), "Je vous remercie")


class TestFr2En(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(french_to_english(""),)
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")
        self.assertEqual(french_to_english("Je vous remercie"), "Thank you.")

"""Diferent tests for the translator. There are:
-One for the null value.
-One for Hello-Bonjour and another for the Bonjour-Hello.
-Two more of my own to improve my tests."""
unittest.main()