import unittest
from math import pi

from circlinator_upload.src.circle import circle


class TestCirclinator(unittest.TestCase):

    def test_circumference(self):
        self.assertEqual(circle.circlinate(3)[1], 6 * pi)
        self.assertEqual(circle.circlinate(5)[1], 10 * pi)
        self.assertEqual(circle.circlinate(10)[1], 20 * pi)

    def test_area(self):
        self.assertEqual(circle.circlinate(3)[0], 9 * pi)
        self.assertEqual(circle.circlinate(5)[0], 25 * pi)
        self.assertEqual(circle.circlinate(10)[0], 100 * pi)