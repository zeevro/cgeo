# zeevro-cgeo
A Python C extension module with geographic functions

This library has two functions:

* `great_circle_distance(s_lat, s_lng, d_lat, d_lng)`: Returns the distance between two coordinates on earth
* `point_inside_polygon(x, y, [(x1, y1), (x2, y2), ...])`: Returns a `bool` denoting whether the point `(x, y)` is inside the polygon `[(x1, y1), (x2, xy), ...]`
