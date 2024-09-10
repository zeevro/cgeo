try:
    from ._cgeo import great_circle_distance, point_inside_polygon
except ImportError:
    import warnings
    warnings.warn('Could not import cgeo C extension, Using slow fallback.')
    from ._cgeo_slow import great_circle_distance, point_inside_polygon


__all__ = ['great_circle_distance', 'point_inside_polygon']
