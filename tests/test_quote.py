
import unittest
from quote import quote
class NewsTest(unittest.TestCase) :
    def setUp(self):
        self.new_news = quote('')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,quote)) 


    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
        
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password("banana"))
                

