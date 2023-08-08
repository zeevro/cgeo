from math import atan2, cos, pow, radians, sin, sqrt


EARTH_RADIUS = 6378.137  # km


def great_circle_distance(s_lat, s_lng, d_lat, d_lng):
    s_lat = radians(s_lat)
    s_lng = radians(s_lng)
    d_lat = radians(d_lat)
    d_lng = radians(d_lng)

    sin_s_lat = sin(s_lat)
    cos_s_lat = cos(s_lng)
    sin_d_lat = sin(d_lat)
    cos_d_lat = cos(d_lng)

    delta_lng = d_lng - s_lng
    sin_delta_lng = sin(delta_lng)
    cos_delta_lng = cos(delta_lng)

    return atan2(
        sqrt(
            pow((cos_d_lat * sin_delta_lng), 2) +
            pow((cos_s_lat * sin_d_lat - sin_s_lat * cos_d_lat * cos_delta_lng) ,2)
        ),
        sin_s_lat * sin_d_lat + cos_s_lat * cos_d_lat * cos_delta_lng
    ) * EARTH_RADIUS


def point_inside_polygon(x, y, poly):
    c = False
    for (ix, iy), (jx, jy) in zip(poly, [poly[-1], *poly[:-1]]):
        if ((iy > y) != (jy > y)) and (x < (jx - ix) * (y - iy) / (jy - iy) + ix):
            c = not c
    return c
