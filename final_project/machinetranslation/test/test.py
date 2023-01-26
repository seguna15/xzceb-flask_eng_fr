import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrenchWithNullInput(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(), 'Bonjour') # Testing english to french with null value

class TestFrenchWithNullInput(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(), 'Hello') # Testing french to english with null value


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test if Hello translates to Bonjour
        

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test if Bonjour translates to Hello

unittest.main()