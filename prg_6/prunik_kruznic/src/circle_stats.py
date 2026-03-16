import math

def radius_sum(r1, r2):
    return r1 + r2

def euclid_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def has_intersection(circle_1, circle_2):
    x1 =  circle_1["x"]
    y1 =  circle_1["y"]
    r1 =  circle_1["r"]

    x2 = circle_2["x"]
    y2 = circle_2["y"]
    r2 = circle_2["r"]

    d = euclid_distance(x1, y1, x2, y2)
    r_sum = radius_sum(r1, r2)
    r_diff = abs(r1 - r2)

    eps = 1e-9

    if math.isclose(d, r_sum, abs_tol=eps) or math.isclose(d, r_diff, abs_tol=eps):
        return {
            "is_intersection": True,
            "intersection_count": 1
        }

    if d > r_sum:
        return {
            "is_intersection": False,
            "intersection_count": 0
        }

    if d < r_diff:
        return {
            "is_intersection": False,
            "intersection_count": 0
        }

    if r_diff < d < r_sum:
        return {
            "is_intersection": True,
            "intersection_count": 2
        }



    if math.isclose(d, 0, abs_tol=eps) and math.isclose(r1, r2, abs_tol=eps):
        return {
            "is_intersection": True,
            "intersection_count": float("inf")
        }

    return {
        "is_intersection": False,
        "intersection_count": 0
    }

if __name__ == "__main__":
    circle_1 = {"x": 0, "y": 0, "r": 2}
    circle_2 = {"x": 3, "y": 0, "r": 1}

    print("radius_sum:", radius_sum(circle_1["r"], circle_2["r"]))
    print("euclid_distance:", euclid_distance(circle_1["x"], circle_1["y"], circle_2["x"], circle_2["y"]))
    print("has_intersection:", has_intersection(circle_1, circle_2))

