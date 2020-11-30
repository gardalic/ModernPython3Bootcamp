import unittest
from robot import Robot


class RobotTest(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)
    def test_charge(self):
        # mega_man = Robot("Mega Man", battery=50)
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        # mega_man = Robot("Mega Man", battery=50)
        self.assertEqual(self.mega_man.say_name(), "BEEP BOOP BEEP BOOP. I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()