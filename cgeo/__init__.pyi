from typing import Iterable, SupportsFloat, Tuple


def great_circle_distance(s_lat: SupportsFloat, s_lng: SupportsFloat, d_lat: SupportsFloat, d_lng: SupportsFloat) -> float:
    """Calculate the geodesian (great-circle) distance between two points. Coordinates are given in degrees."""
    ...


def point_inside_polygon(x: SupportsFloat, y: SupportsFloat, poly: Iterable[Tuple[SupportsFloat, SupportsFloat]]) -> bool:
    """Check whether a point is inside a polygon."""
    ...
