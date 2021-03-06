import unittest
from app.newcrud import User
from app.shoppinglistapp import ShoppingListApp


class TestUserAuthentication(unittest.TestCase):
    """
    Class to test the user authentication, both the registration
    and login.
    """

    def setUp(self):
        self.user = User('hadijah', '12345678', 'had')
        self.app = ShoppingListApp()

    def test_user_is_added_to_dictionary_when_created(self):
        self.assertTrue(self.app.register_user(User('hadijah', '12345678', 'had')))

    def test_user_already_exists_in_user_dictionary(self):
        self.app.users = {'hadijah': self.user}
        self.assertFalse(self.app.register_user(self.user))

    def test_user_sigining_in_is_already_registered(self):
        self.app.users = {'hadijah': self.user}
        self.assertTrue(self.app.does_user_exist('hadijah'))

    def test_user_trying_to_login_has_entered_a_correct_password(self):
        self.app.users = {'hadijah': self.user}
        self.assertTrue(self.app.login_user('hadijah', '12345678'))

    def test_user_trying_to_login_has_entered_a_wrong_password(self):
        self.app.users = {'hadijah': self.user}
        self.assertFalse(self.app.login_user('hadijah', '12341'))


if __name__ == '__main__':
    unittest.main()