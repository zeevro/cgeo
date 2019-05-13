from __future__ import print_function

print()
print('Testing...')
print()

import cgeo

assert cgeo.great_circle_distance(1, 2, 3, 4) == 314.4915326116153
assert cgeo.great_circle_distance(1, 2, 3, 4) == cgeo.great_circle_distance(3, 4, 1, 2)

poly = ((0, 0),
        (0, 2),
        (2, 2),
        (2, 0))

for x, y in [(1, 1), (0.5, 0.5), (1.5, 1.5)]:
    assert cgeo.point_inside_polygon(x, y, poly)
for x, y in [(1, 3), (3, 1), (-1, 1), (1, -1)]:
    assert not cgeo.point_inside_polygon(x, y, poly)

print('Done.')
