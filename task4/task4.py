### Python Program


# Sports Tournament Ranking System

teams = ["Team A", "Team B", "Team C", "Team D"]

# Points system:
# Win  = 3 points
# Draw = 1 point
# Loss = 0 points

# Match results:
# (Team 1, Team 2, Score 1, Score 2)
matches = [
    ("Team A", "Team B", 2, 1),
    ("Team C", "Team D", 1, 1),
    ("Team A", "Team C", 0, 2),
    ("Team B", "Team D", 3, 1),
    ("Team A", "Team D", 2, 2),
    ("Team B", "Team C", 0, 1)
]

# Store team statistics
stats = {}

for team in teams:
    stats[team] = {
        "points": 0,
        "goals_for": 0,
        "goals_against": 0
    }

# Process each match
for team1, team2, score1, score2 in matches:

    stats[team1]["goals_for"] += score1
    stats[team1]["goals_against"] += score2

    stats[team2]["goals_for"] += score2
    stats[team2]["goals_against"] += score1

    if score1 > score2:
        stats[team1]["points"] += 3

    elif score2 > score1:
        stats[team2]["points"] += 3

    else:
        stats[team1]["points"] += 1
        stats[team2]["points"] += 1


# Calculate goal difference
for team in teams:
    stats[team]["goal_difference"] = (
        stats[team]["goals_for"] -
        stats[team]["goals_against"]
    )

# Competition policy:
# 1. Highest points
# 2. Highest goal difference
# 3. Highest goals scored

ranking = sorted(
    teams,
    key=lambda team: (
        stats[team]["points"],
        stats[team]["goal_difference"],
        stats[team]["goals_for"]
    ),
    reverse=True
)

# Display rankings
print("SPORTS TOURNAMENT RANKING")
print("-------------------------")

print("Rank  Team       Points  GF  GA  GD")

for position, team in enumerate(ranking, start=1):
    print(
        position,
        "   ",
        team,
        "    ",
        stats[team]["points"],
        "     ",
        stats[team]["goals_for"],
        "  ",
        stats[team]["goals_against"],
        "  ",
        stats[team]["goal_difference"]
    )
