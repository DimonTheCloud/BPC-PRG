from acc_activity import get_magnitude_signal


file0_acc_xyz_signal = [(1.47, -2.19, 9.81), (-0.13, 2.26, 9.81), (0.41, -1.91, 9.81), (-2.48, -1.43, 9.81), (-0.09, 0.1, 9.82), (-0.1, 0.16, 9.86), (1.05, -2.65, 9.8), (-1.24, -9.75, 0.04)]
file0_magnitude_signal = [10.15840046464009, 10.067800156935974, 10.00261465817813, 10.219168263611282, 9.820921545354082, 9.86180510859954, 10.206125611611883, 9.828616382787558]

file1_acc_xyz_signal = [(-0.01, -0.16, 9.8), (0.04, 0.17, 9.86), (-0.01, 0.15, 9.79), (0.12, 0.02, 9.76), (0.09, -0.04, 9.84), (0.07, -0.2, 9.81), (1.26, -1.38, 9.8), (6.73, -7.12, 0.01), (0.7, 9.8, 0.06), (-9.27, 3.14, -0.04)]
file1_magnitude_signal = [9.801311136781651, 9.861546531857972, 9.791154170985154, 9.760758167273687, 9.84049287383513, 9.812288214274997, 9.976572557747476, 9.797315958975704, 9.825151398324609, 9.787446040719713]

example_acc_xyz_signal = [(0.11, -0.08, 9.8), (-0.14, 0.01, 9.81), (0.03, 0.04, 9.82), (2.2, 3.3, 9.82), (-0.11, -0.22, 9.84), (-0.11, -9.85, 0.12)]
example_magnitude_signal = [9.800943832101071, 9.811004026092336, 9.82012729041737, 10.590675143729035, 9.84307370692712, 9.851345085824574]


def test_get_magnitude_signal():
    def round_sig(signal, n=2):
        return [round(x, n) for x in signal]
    assert round_sig(get_magnitude_signal(example_acc_xyz_signal)) == round_sig(example_magnitude_signal) 
    assert round_sig(get_magnitude_signal(file0_acc_xyz_signal)) == round_sig(file0_magnitude_signal) 
    assert round_sig(get_magnitude_signal(file1_acc_xyz_signal))  == round_sig(file1_magnitude_signal) 
