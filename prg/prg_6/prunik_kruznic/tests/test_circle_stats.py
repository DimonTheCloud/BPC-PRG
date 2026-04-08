from circle_stats import has_intersection


def test_has_intersection_two_points():
    circle_1 = {"x": 0, "y": 0, "r": 3}
    circle_2 = {"x": 4, "y": 0, "r": 3}

    expected = {"is_intersection": True, "intersections_count": 2}
    assert has_intersection(circle_1, circle_2) == expected


def test_has_intersection_no_points():
    circle_1 = {"x": 0, "y": 0, "r": 2}
    circle_2 = {"x": 10, "y": 0, "r": 2}

    expected = {"is_intersection": False, "intersections_count": 0}
    assert has_intersection(circle_1, circle_2) == expected


def test_has_intersection_external_tangent():
    circle_1 = {"x": 0, "y": 0, "r": 2}
    circle_2 = {"x": 4, "y": 0, "r": 2}

    expected = {"is_intersection": True, "intersections_count": 1}
    assert has_intersection(circle_1, circle_2) == expected


def test_has_intersection_internal_tangent():
    circle_1 = {"x": 0, "y": 0, "r": 5}
    circle_2 = {"x": 2, "y": 0, "r": 3}

    expected = {"is_intersection": True, "intersections_count": 1}
    assert has_intersection(circle_1, circle_2) == expected


def test_has_intersection_negative_radius():
    circle_1 = {"x": 0, "y": 0, "r": -2}
    circle_2 = {"x": 4, "y": 0, "r": 2}

    try:
        has_intersection(circle_1, circle_2)
        assert False, "Expected ValueError for negative radius"
    except ValueError:
        assert True