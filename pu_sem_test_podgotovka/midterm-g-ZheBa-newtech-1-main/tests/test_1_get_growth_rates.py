from cell_growth import get_growth_rates


def test_get_growth_rates():
    assert get_growth_rates([0, 1, 2, 3, 4], [100, 110, 150, 260, 265]) == [10.0, 40.0, 110.0, 5.0]
    assert get_growth_rates([0, 2, 4], [50, 90, 170]) == [20.0, 40.0]
    assert get_growth_rates([1, 3, 6], [200, 200, 260]) == [0.0, 20.0]
    