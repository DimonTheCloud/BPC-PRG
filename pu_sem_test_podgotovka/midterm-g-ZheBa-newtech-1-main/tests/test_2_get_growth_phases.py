from cell_growth import get_growth_phases


def test_get_growth_phases():
    assert get_growth_phases([10.0, 40.0, 110.0, 5.0]) == ['stationary', 'lag', 'log', 'stationary']
    assert get_growth_phases([19.9, 20.0, 80.0, 80.1]) == ['stationary', 'lag', 'lag', 'log']
    assert get_growth_phases([0.0, -5.0, 30.0]) == ['stationary', 'stationary', 'lag']
    