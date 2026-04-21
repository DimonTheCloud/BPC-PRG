from cell_growth import get_peak_growth_interval


def test_get_peak_growth_interval():
    assert get_peak_growth_interval([0, 1, 2, 3, 4], [10.0, 40.0, 110.0, 5.0]) == (2, 3, 110.0)
    assert get_peak_growth_interval([0, 2, 4], [15.0, 45.0]) == (2, 4, 45.0)
    assert get_peak_growth_interval([0, 1, 3, 6], [50.0, 50.0, 20.0]) == (0, 1, 50.0)
    