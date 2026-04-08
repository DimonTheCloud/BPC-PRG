import matplotlib.pyplot as plt


def load_signal_from_txt(path):
    values = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                values.append(float(line))

    return values


def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values) / len(values)


def plot_signal(values):
    plt.plot(values)
    plt.title("EKG signal")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    signal_values = load_signal_from_txt("ekg_signal.txt")

    print("MIN:", signal_min(signal_values))
    print("MAX:", signal_max(signal_values))
    print("AVG:", signal_avg(signal_values))

    plot_signal(signal_values)







