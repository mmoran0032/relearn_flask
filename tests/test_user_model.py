

import unittest

from app.models import User


class UserModelTest(unittest.TestCase):
    def test_password_setter(self):
        user = User(password='laura')
        self.assertTrue(user.password_hash is not None)

    def test_password_unreadable(self):
        user = User(password='laura')
        with self.assertRaises(AttributeError):
            user.password

    def test_password_verification(self):
        user = User(password='laura')
        self.assertTrue(user.verify_password('laura'))
        self.assertFalse(user.verify_password('link'))

    def test_password_salts_random(self):
        user_one = User(password='laura')
        user_two = User(password='laura')
        self.assertNotEqual(user_one.password_hash, user_two.password_hash)
