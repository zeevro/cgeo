import unittest

import cgeo


class TestGreatCircleDistance(unittest.TestCase):
    def test_literal(self):
        self.assertEqual(cgeo.great_circle_distance(1, 2, 3, 4), 314.7551553654009)

    def test_order(self):
        self.assertEqual(cgeo.great_circle_distance(1, 2, 3, 4), cgeo.great_circle_distance(3, 4, 1, 2))


class TestPointInPolygon(unittest.TestCase):
    poly = ((0, 0),
            (0, 2),
            (2, 2),
            (2, 0))

    def test_inside(self):
        for x, y in [(1, 1), (0.5, 0.5), (1.5, 1.5)]:
            self.assertTrue(cgeo.point_inside_polygon(x, y, self.poly))

    def test_outside(self):
        for x, y in [(1, 3), (3, 1), (-1, 1), (1, -1)]:
            self.assertFalse(cgeo.point_inside_polygon(x, y, self.poly))


if __name__ == "__main__":
    unittest.main()
