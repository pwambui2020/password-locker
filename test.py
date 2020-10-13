import unittest
from main import User,Credentials
class TestMain(unittest.TestCase):
    def setUp(self):
        self.user=User('Paulyne','2020')
        self.cred=Credentials('facebook','Wambui','1989')
    def test_user(self):
        self.assertEqual(self.user.username,'Paulyne')
        self.assertEqual(self.user.password,'2020')

    def test_credentials(self):
        self.assertEqual(self.cred.site,'facebook')
        self.assertEqual(self.cred.username,'Wambui')
        self.assertEqual(self.cred.password,'1989')
       

if __name__=='__main__':
    unittest.main()

