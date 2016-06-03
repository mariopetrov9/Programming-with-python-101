import sys
import unittest
import os

sys.path.append("..")


import sql_manager
import helpers


STRONG_PASSWORD1 = "123Asdf$$123Asdf"
STRONG_PASSWORD2 = "321$$321Asdf"


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_database()
        sql_manager.register('Tester', STRONG_PASSWORD1)

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        sql_manager.register('Dinko', STRONG_PASSWORD2)

        sql_manager.cursor.execute('''SELECT Count(*)
                                    FROM clients
                                    WHERE username = ?''', ('Dinko',))
        sql_manager.db.commit()
        users_count = sql_manager.cursor.fetchone()
        self.assertEqual(users_count[0], 1)

    # def test_login_sql_injection_in_password(self):
    #     logged_user = sql_manager.login('Tester', "' OR 1=1 --")
    #     self.assertFalse(logged_user)

    # def test_login_sql_injection_in_username(self):
    #     logged_user = sql_manager.login("' OR 1=1 --", "blqblq")
    #     self.assertFalse(logged_user)

    # def test_login(self):
        # logged_user = sql_manager.login('Tester', STRONG_PASSWORD1)
        # self.assertEqual(logged_user.get_username(), 'Tester')

    # def test_login_wrong_password(self):
    #     logged_user = sql_manager.login('Tester', '123567')
    #     self.assertFalse(logged_user)

    # def test_change_message(self):
    #     logged_user = sql_manager.login('Tester', '123')
    #     new_message = "podaivinototam"
    #     sql_manager.change_message(new_message, logged_user)
    #     self.assertEqual(logged_user.get_message(), new_message)

    # def test_change_password(self):
    #     logged_user = sql_manager.login('Tester', '123')
    #     new_password = "12345"
    #     sql_manager.change_pass(new_password, logged_user)

    #     logged_user_new_password = sql_manager.login('Tester', new_password)
    #     self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    # def test_change_password_with_sql_injection(self):
    #     sql_manager.register("Dinko", "123")
    #     sql_manager.register("VLadko", "321")

    #     logged_user = sql_manager.login('Dinko', '123')
    #     new_password = "1234' WHERE id = 3 --"
    #     sql_manager.change_pass(new_password, logged_user)

    #     self.assertFalse(sql_manager.login('VLadko', '1234'))

    # def test_validate_password_more_than_8_symbols(self):
    #     password = '1231232326584'
    #     self.assertTrue(start.validate(password))

    # def test_validate_password_special_symbol(self):
    #     password = "123156488$"
    #     self.assertTrue(start.validate(password, "safc"))

    def test_valitate_password(self):
        password = "321$$321Asdf"
        validator = helpers.validate("krasi", password)
        self.assertTrue(validator.is_valid(password))


if __name__ == '__main__':
    unittest.main()
