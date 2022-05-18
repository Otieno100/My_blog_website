
import unittest
from quote import quote
class NewsTest(unittest.TestCase) :
    def setUp(self):
        self.new_news = quote('')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,quote))   
