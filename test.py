from __future__ import print_function

print()
print('Testing...')
print()

import cgeo

assert cgeo.great_circle_distance(1, 2, 3, 4) == cgeo.great_circle_distance(3, 4, 1, 2)

poly = ((0, 0),
        (0, 2),
        (2, 2),
        (2, 0),
        (0, 0))

assert cgeo.point_inside_polygon(1, 1, poly)
assert not cgeo.point_inside_polygon(4, 4, poly)

print('Done.')
