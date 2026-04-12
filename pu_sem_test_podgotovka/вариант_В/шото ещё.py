import csv

MODELS = {
    "301": {"avg_height": 1.75, "avg_weight": 72.0},
    "302": {"avg_height": 1.60, "avg_weight": 55.0}
}

CATEGORIES = [
    ("S", 0, 89),
    ("M", 90, 109),
    ("L", 110, 999)
]

MAX_HEIGHT = 2
MAX_WEIGHT = 2
MAX_STATS = 30


def load_players(path):
    data = []

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            player = {
                'name': row[0],
                'id': row[1],
                'height': float(row[2]),
                'weight': float(row[3]),
                'stats': (int(row[4]), int(row[5]), int(row[6]))
            }
            data.append(player)
    return data

def select_players_by_id(players, player_id):
    result = []

    for player in players:
        if player['id'] == player_id:
            result.append(player)

    return result



def assign_category(player, models):
    avg_height = models[player['id']]['avg_height']
    percent = player["height"] / avg_height * 100

    for name, lower, upper in CATEGORIES:
        if lower <= percent <= upper:
            player['category'] = name
            return player


    player['category'] = None
    return player



def get_score(player, models):
    avg_height = models[player["id"]]["avg_height"]
    avg_weight = models[player["id"]]["avg_weight"]


    scaled_height = (player["height"] / avg_height) / MAX_HEIGHT
    scaled_weight = (player["weight"] / avg_weight) / MAX_WEIGHT
    scaled_stats = sum(player["stats"]) / MAX_STATS

    score = scaled_height * 50 + scaled_weight * 30 + scaled_stats * 20

    player['score'] = round(score)

    return player

def main(path, player_id):
    players = load_players(path)
    players = select_players_by_id(players, player_id)

    result = []

    for player in players:
        player = assign_category(player, MODELS)
        player = get_score(player, MODELS)
        result.append(player)

    return result















