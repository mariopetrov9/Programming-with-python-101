from weapon import Weapon
import unittest

class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon("gun", 40)

    def test_damage(self):
        self.assertEqual(self.weapon.get_damage(), 40)

    def test_name(self):
        self.assertEqual(self.weapon.get_name(), 'gun')

if __name__ == "__main__":
        unittest.main()
