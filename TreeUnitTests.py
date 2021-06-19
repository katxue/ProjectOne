import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_calc_base(self):
        color, rect = main.calc_base((100, 100), 10, 50, (255, 255, 255))
        self.assertEqual((255, 255, 255), color)
        self.assertEqual(((100, 90), (50, 10)), rect)


if __name__ == '__main__':
    unittest.main()
