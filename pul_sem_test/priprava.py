import json, csv


SIZE_CATEGORIES = [
    ("XS", 0, 79),
    ("M", 80, 119),
    ("L", 120, 159),
    ("XL", 160, 220)
]

MAX_SIZE = 2
MAX_WEIGHT = 2
MAX_SKILLS = 30

def load_types(path):
    with open(path, encoding = 'UTF-8') as f:
        types = json.load(f)

    return types

def load_artifacts(path):
    data = []

    with open(path, encoding = 'UTF-8') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            artifact = {
                "name": row[0],
                "id": row[1],
                "size": float(row[2]),
                "weight": float(row[3]),
                "stats": (int(row[4]), int(row[5]), int(row[6]))
            }
            data.append(artifact)

    return data


def assign_size_category(artifact, types_data):
    avg_size = types_data[artifact["id"]]["avg_size"]
    percent = artifact["size"] / avg_size * 100
    for name, lower, upper in SIZE_CATEGORIES:
        if lower <= percent <= upper:
            artifact["category"] = name
            return artifact

    artifact["category"] = None
    return artifact



def get_score(artifact, types_data):






    avg_size = types_data[artifact["id"]]["avg_size"]
    avg_weight = types_data[artifact["id"]]["avg_weight"]

    scaled_size = (artifact["size"] / avg_size) / MAX_SIZE
    scaled_weight = (artifact["weight"] / avg_weight) / MAX_WEIGHT
    scaled_stats = sum(artifact["stats"]) / MAX_SKILLS

    score = scaled_size * 50 + scaled_weight * 30 + scaled_stats * 20

