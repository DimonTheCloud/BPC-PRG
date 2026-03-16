from prg_6.EKG_test import signal_plot_ops

values = signal_plot_ops.load_signal_from_txt("ekg_signal.txt")

print("AVG:", signal_plot_ops.signal_avg(values))

signal_plot_ops.plot_signal(values)