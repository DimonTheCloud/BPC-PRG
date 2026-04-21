from cell_growth import read_growth_data


def test_read_growth_data(tmp_path):
    file_path = tmp_path / "test.csv"

    file_path.write_text(
        """experiment_id,strain,temperature_c,time_hours,cell_count
EXP001,E.coli,37.0,0,100
EXP001,E.coli,37.0,1,120
EXP001,E.coli,37.0,2,200
""",
        encoding='utf-8',
    )
    times, cell_counts = read_growth_data(file_path)
    assert times == [0.0, 1.0, 2.0]
    assert cell_counts == [100.0, 120.0, 200.0]

    file_path.write_text(
        """time_hours,cell_count
0,50
2,90
5,180
""",
        encoding='utf-8',
    )
    times, cell_counts = read_growth_data(file_path)
    assert times == [0.0, 2.0, 5.0]
    assert cell_counts == [50.0, 90.0, 180.0]

    file_path.write_text(
        """strain,time_hours,cell_count,temperature_c
yeast,0,10,28.0
yeast,1.5,25,28.0
yeast,3,55,28.0
""",
        encoding='utf-8',
    )
    times, cell_counts = read_growth_data(file_path)
    assert times == [0.0, 1.5, 3.0]
    assert cell_counts == [10.0, 25.0, 55.0]
    