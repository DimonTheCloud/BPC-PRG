from circle_stats import has_intersection
from circles_intersection_draw import draw_data


circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}

result = has_intersection(circle_1, circle_2)

print("Výsledek:", result)

if result["is_intersection"]:
    if result["intersections_count"] == 1:
        print("Kružnice se protínají a mají 1 průnik.")
    elif result["intersections_count"] == 2:
        print("Kružnice se protínají a mají 2 průniky.")
    elif result["intersections_count"] == float("inf"):
        print("Kružnice jsou totožné a mají nekonečně mnoho společných bodů.")
else:
    print("Kružnice se neprotínají a mají 0 průniků.")

draw_data(circle_1, circle_2)