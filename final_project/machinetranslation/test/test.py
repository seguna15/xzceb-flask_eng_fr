import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test if Hello translates to Bonjour
        self.assertNotEqual(english_to_french('Hello'), 'Ciao') # test if Hello is not equal to Ciao
class TestingFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test if Bonjour translates to Hello
        self.assertNotEqual(french_to_english('Bonjour'), 'Bye') # test if Bonjour is not equal to Bye
unittest.main()