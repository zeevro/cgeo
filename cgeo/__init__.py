from __future__ import annotations

from typing import TYPE_CHECKING, Iterable


if TYPE_CHECKING:

    def great_circle_distance(s_lat: float, s_lng: float, d_lat: float, d_lng: float) -> float:  # noqa: ARG001
        """Calculate the geodesian (great-circle) distance between two points. Coordinates are given in degrees."""

    def point_inside_polygon(x: float, y: float, poly: Iterable[tuple[float, float]]) -> bool:  # noqa: ARG001
        """Check whether a point is inside a polygon."""
else:
    try:
        from ._cgeo import great_circle_distance, point_inside_polygon
    except ImportError:
        import warnings

        warnings.warn('Could not import cgeo C extension, Using slow fallback.')
        from ._cgeo_slow import great_circle_distance, point_inside_polygon


__all__ = ['great_circle_distance', 'point_inside_polygon']
