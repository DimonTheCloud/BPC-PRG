import json, csv


SIZE_CLASSES = [
    ("XS", 0, 79),
    ("M", 80, 119),
    ("L", 120, 159),
    ("XL", 160, 220)
]

MAX_HEIGHT = 2
MAX_WEIGHT = 2
MAX_STATS = 30


def load_models(path):
    with open(path, "r", encoding="utf-8") as f:
        models = json.load(f)

    return models

def load_robots(path):

    data = []

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            robot = {
                "name": row[0],
                "id": row[1],
                "height": float(row[2]),
                "weight": float(row[3]),
                "stats": (int(row[4]), int(row[5]), int(row[6]))
            }
            data.append(robot)

        return data

def assign_size_class(robot, models_data):
    avg_height = models_data[robot["id"]]["avg_height"]
    percent = robot["height"] / avg_height * 100

    for name, lower, upper in SIZE_CLASSES:
        if lower <= percent <= upper:
            robot["size_class"] = name
            return robot

    robot["size_class"] = None
    return robot


def get_score(robot, models_data):
    avg_height = models_data[robot["id"]]["avg_height"]
    avg_weight = models_data[robot["id"]]["avg_weight"]


    scaled_height = (robot["height"] / avg_height) / MAX_HEIGHT
    scaled_weight = (robot["weight"] / avg_weight) / MAX_WEIGHT

    scaled_stats = sum(robot["stats"]) / MAX_STATS

    score = (
            scaled_height * 50
            + scaled_weight * 30
            + scaled_stats * 20
    )

    robot["score"] = round(score)
    return robot


def selected_robots(all_robots, models_data, robot_id, size_class):
    result = []
    for robot in all_robots:
        if robot["id"] == robot_id:
            robot = assign_size_class(robot, models_data)
            if robot["size_class"] == size_class:
                robot = get_score(robot, models_data)
                result.append(robot)

    return result

def get_winner(robots):
    if len(robots) == 0:
        return None

    best = robots[0]

    for robot in robots:
        if robot["score"] > best["score"]:
            best = robot

    return best["name"]

def main(models_path, robots_path, robot_id, size_class):
    models_data = load_models(models_path)
    robots = load_robots(robots_path)
    selected = selected_robots(robots, models_data, robot_id, size_class)

    if len(selected) == 0:
        return "No matching robots found."

    winner = get_winner(selected)
    return selected, winner



