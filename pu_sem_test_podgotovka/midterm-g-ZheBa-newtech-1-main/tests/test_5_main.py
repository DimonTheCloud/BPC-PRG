from cell_growth import main


def test_main_prints_growth_analysis(tmp_path, capsys):
    file_path = tmp_path / "test.csv"

    file_path.write_text(
        """experiment_id,strain,temperature_c,time_hours,cell_count
EXP_TEST,test_strain,37.0,0,100
EXP_TEST,test_strain,37.0,1,120
EXP_TEST,test_strain,37.0,2,200
EXP_TEST,test_strain,37.0,3,290
EXP_TEST,test_strain,37.0,4,295
""",
        encoding='utf-8',
    )
    main(file_path)
    captured = capsys.readouterr()
    assert captured.out == (
        "Times: [0.0, 1.0, 2.0, 3.0, 4.0]\n"
        "Cell counts: [100.0, 120.0, 200.0, 290.0, 295.0]\n"
        "Growth rates: [20.0, 80.0, 90.0, 5.0]\n"
        "Growth phases: ['lag', 'lag', 'log', 'stationary']\n"
        "Peak growth interval: 2.0-3.0 h\n"
        "Peak growth rate: 90.0\n"
    )

    file_path.write_text(
        """time_hours,cell_count,experiment_id
0,50,EXP002
2,70,EXP002
4,130,EXP002
6,290,EXP002
8,300,EXP002
""",
        encoding='utf-8',
    )
    main(file_path)
    captured = capsys.readouterr()
    assert captured.out == (
        "Times: [0.0, 2.0, 4.0, 6.0, 8.0]\n"
        "Cell counts: [50.0, 70.0, 130.0, 290.0, 300.0]\n"
        "Growth rates: [10.0, 30.0, 80.0, 5.0]\n"
        "Growth phases: ['stationary', 'lag', 'lag', 'stationary']\n"
        "Peak growth interval: 4.0-6.0 h\n"
        "Peak growth rate: 80.0\n"
    )
    