from circle_stats import radius_sum

def test_radius_sum_basic():
    r1 = 2
    r2 = 3
    expected = 5

    assert radius_sum(r1, r2) == expected