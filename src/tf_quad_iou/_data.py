from dataclasses import dataclass
import numpy as np
import math


@dataclass
class SegmentIntersectionData:
    Segment1: np.ndarray
    Segment2: np.ndarray
    Expected: np.ndarray


SEGMENT_INTERSECTIONS = [
    SegmentIntersectionData(
        Segment1=np.array([[0, 0], [0, 1]], dtype=np.float32),
        Segment2=np.array([[0, 0], [1, 0]], dtype=np.float32),
        Expected=np.array([[0, 0]], dtype=np.float32),
    ),
    SegmentIntersectionData(
        Segment1=np.array([[0, 0], [1, 1]], dtype=np.float32),
        Segment2=np.array([[1, 0], [0, 1]], dtype=np.float32),
        Expected=np.array([[0.5, 0.5]], dtype=np.float32),
    ),
    # co-linear condition
    SegmentIntersectionData(
        Segment1=np.array([[0, 0], [0, 1]], dtype=np.float32),
        Segment2=np.array([[0, 0], [0, 2]], dtype=np.float32),
        Expected=np.array([[]], dtype=np.float32),
    ),
    SegmentIntersectionData(
        Segment1=np.array([[0, 0], [0, 1]], dtype=np.float32),
        Segment2=np.array([[1, 0], [1, 1]], dtype=np.float32),
        Expected=np.array([[]], dtype=np.float32),
    ),
    # intersection outside of segment
    SegmentIntersectionData(
        Segment1=np.array([[0, 0], [0, 1]], dtype=np.float32),
        Segment2=np.array([[1, 1], [2, 1]], dtype=np.float32),
        Expected=np.array([[]], dtype=np.float32),
    ),
    SegmentIntersectionData(
        Segment1=np.array([[0, 0], [0, 1]], dtype=np.float32),
        Segment2=np.array([[3, 2], [2, 2]], dtype=np.float32),
        Expected=np.array([[]], dtype=np.float32),
    ),
]


@dataclass
class PointsInPolygonData:
    Polygon: np.ndarray
    Points: np.ndarray
    Expected: np.ndarray


POINT_IN_QUADS = [
    # -- With a square --
    PointsInPolygonData(
        np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]], dtype=np.float32),
        np.array(
            [
                [0, 0],
                [1, 2],
                [1, -2],
                [-1, -1],
                [1, 1],
                [-1, 1],
                [1, -1],
                [0, 1],
                [0, -1],
                [-1, 0],
                [1, 0],
            ],
            dtype=np.float32,
        ),
        np.array(
            [
                True,
                False,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
            ],
            dtype=bool,
        ),
    ),
    # -- With an hourglass --
    # just above the center is inside
    PointsInPolygonData(
        np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]], dtype=np.float32),
        np.array(
            [
                [0.0, 1.0e-6],
                [1.0e-6, 0.0],
                [0.0, 0.0],
                [-1, -1],
                [1, 1],
                [-1, 1],
                [1, -1],
                [0, 1],
                [0, -1],
                [-1, 0],
                [1, 0],
            ],
            dtype=np.float32,
        ),
        np.array(
            [
                True,
                False,
                False,
                True,
                True,
                True,
                True,
                True,
                True,
                False,
                False,
            ],
            dtype=bool,
        ),
    ),
]


@dataclass
class BoxesIntersectionData:
    Box1: np.ndarray
    Box2: np.ndarray
    Expected: np.ndarray


sqrt2 = math.sqrt(2)
BOX_INTERSECTIONS = [
    BoxesIntersectionData(
        Box1=np.array(
            [
                [-1, -1],
                [-1, 1],
                [1, 1],
                [1, -1],
            ],
            dtype=np.float32,
        ),
        Box2=np.array(
            [
                [-1, -1],
                [-1, 1],
                [1, 1],
                [1, -1],
            ],
            dtype=np.float32,
        ),
        Expected=np.array(
            [
                [-1, -1],
                [1, -1],
                [1, 1],
                [-1, 1],
            ],
            dtype=np.float32,
        ),
    ),
    BoxesIntersectionData(
        Box1=np.array(
            [
                [-1, -1],
                [-1, 1],
                [1, 1],
                [1, -1],
            ],
            dtype=np.float32,
        ),
        Box2=np.array(
            [
                [0, 0],
                [0, 2],
                [2, 2],
                [2, 0],
            ],
            dtype=np.float32,
        ),
        Expected=np.array(
            [
                [0, 0],
                [1, 0],
                [1, 1],
                [0, 1],
            ],
            dtype=np.float32,
        ),
    ),
    BoxesIntersectionData(
        Box1=np.array(
            [
                [-1, -1],
                [-1, 1],
                [1, 1],
                [1, -1],
            ],
            dtype=np.float32,
        ),
        Box2=np.array(
            [
                [0, sqrt2],
                [sqrt2, 0],
                [0, -sqrt2],
                [-sqrt2, 0],
            ],
            dtype=np.float32,
        ),
        Expected=np.array(
            [
                [-1, -sqrt2 + 1],
                [-sqrt2 + 1, -1],
                [sqrt2 - 1, -1],
                [1, -sqrt2 + 1],
                [1, sqrt2 - 1],
                [sqrt2 - 1, 1],
                [-sqrt2 + 1, 1],
                [-1, sqrt2 - 1],
            ],
            dtype=np.float32,
        ),
    ),
    BoxesIntersectionData(
        Box1=np.array(
            [
                [-1, -1],
                [-1, 1],
                [1, 1],
                [1, -1],
            ],
            dtype=np.float32,
        ),
        Box2=np.array(
            [
                [-1, 1],
                [0, 0],
                [1, 0],
                [2, 1],
            ],
            dtype=np.float32,
        ),
        Expected=np.array(
            [
                [0, 0],
                [1, 0],
                [1, 1],
                [-1, 1],
            ],
            dtype=np.float32,
        ),
    ),
    BoxesIntersectionData(
        Box1=np.array(
            [
                [-1, -1],
                [-1, 1],
                [1, 1],
                [1, -1],
            ],
            dtype=np.float32,
        ),
        Box2=np.array(
            [
                [1, 1],
                [2, 1],
                [2, 2],
                [1, 2],
            ],
            dtype=np.float32,
        ),
        Expected=np.array(
            [
                [1, 1],
            ],
            dtype=np.float32,
        ),
    ),
    BoxesIntersectionData(
        Box1=np.array(
            [
                [0, 0],
                [8, 0],
                [8, 10],
                [0, 10],
            ],
            dtype=np.float32,
        ),
        Box2=np.array(
            [
                [0, 0],
                [6, 0],
                [6, 8],
                [0, 8],
            ],
            dtype=np.float32,
        ),
        Expected=np.array(
            [
                [0, 0],
                [6, 0],
                [6, 8],
                [0, 8],
            ],
            dtype=np.float32,
        ),
    ),
]


@dataclass
class PolygonArea:
    Polygon: np.ndarray
    Area: np.float32


POLYGON_AREA = [
    PolygonArea(
        Polygon=np.array(
            [
                [0, 0],
                [0, 1],
                [1, 1],
                [1, 0],
            ],
            dtype=np.float32,
        ),
        Area=1,
    ),
    PolygonArea(
        Polygon=np.array(
            [
                [0, 0],
                [0, 0],
                [0, 1],
                [0, 1],
                [1, 1],
                [1, 1],
                [1, 0],
                [1, 0],
            ],
            dtype=np.float32,
        ),
        Area=1,
    ),
]
