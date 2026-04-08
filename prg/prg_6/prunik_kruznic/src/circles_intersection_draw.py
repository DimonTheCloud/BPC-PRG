import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):
    fig, ax = plt.subplots()

    c1 = plt.Circle(
        (circle_1["x"], circle_1["y"]),
        circle_1["r"],
        fill=False,
        color="blue",
        linewidth=2,
        label="circle_1"
    )

    c2 = plt.Circle(
        (circle_2["x"], circle_2["y"]),
        circle_2["r"],
        fill=False,
        color="red",
        linewidth=2,
        label="circle_2"
    )

    ax.add_patch(c1)
    ax.add_patch(c2)

    # vykreslení středů
    ax.plot(circle_1["x"], circle_1["y"], "bo")
    ax.plot(circle_2["x"], circle_2["y"], "ro")

    # rozsah grafu, aby byly kružnice dobře vidět
    min_x = min(circle_1["x"] - circle_1["r"], circle_2["x"] - circle_2["r"]) - 1
    max_x = max(circle_1["x"] + circle_1["r"], circle_2["x"] + circle_2["r"]) + 1
    min_y = min(circle_1["y"] - circle_1["r"], circle_2["y"] - circle_2["r"]) - 1
    max_y = max(circle_1["y"] + circle_1["r"], circle_2["y"] + circle_2["r"]) + 1

    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)

    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Circles intersection")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.show()


if __name__ == "__main__":
    circle_1 = {"x": 0, "y": 0, "r": 2}
    circle_2 = {"x": 3, "y": 0, "r": 1}

    draw_data(circle_1, circle_2)