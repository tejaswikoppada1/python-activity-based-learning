### Python Program


# Multi-Event Sports Scheduling and Scoring

# Teams
teams = ["Team A", "Team B", "Team C", "Team D"]

# Event schedule stored as tuples:
# (Event, Day, Time, Team 1, Team 2)

schedule = [
    ("Football", "Monday", "10:00", "Team A", "Team B"),
    ("Basketball", "Monday", "10:00", "Team A", "Team C"),
    ("Volleyball", "Monday", "11:00", "Team B", "Team D"),
    ("Football", "Tuesday", "10:00", "Team C", "Team D"),
    ("Basketball", "Tuesday", "11:00", "Team A", "Team D"),
    ("Volleyball", "Tuesday", "12:00", "Team B", "Team C")
]

# Match results:
# (Event, Team 1, Team 2, Score 1, Score 2)

results = [
    ("Football", "Team A", "Team B", 2, 1),
    ("Basketball", "Team A", "Team C", 60, 55),
    ("Volleyball", "Team B", "Team D", 1, 2),
    ("Football", "Team C", "Team D", 0, 0),
    ("Basketball", "Team A", "Team D", 70, 65),
    ("Volleyball", "Team B", "Team C", 2, 1)
]

# -------------------------------
# 1. Check scheduling conflicts
# -------------------------------

print("SCHEDULE")
print("--------")

occupied_slots = set()

for event, day, time, team1, team2 in schedule:

    slot = (day, time)

    # Check whether either team is already playing
    team_conflict = False

    for existing in occupied_slots:
        if existing[0] == day and existing[1] == time:
            if team1 in existing[2] or team2 in existing[2]:
                team_conflict = True

    if team_conflict:
        print("CONFLICT:", event, team1, "vs", team2)
    else:
        print(event, "-", day, time, "-", team1, "vs", team2)
        occupied_slots.add((day, time, (team1, team2)))


# -------------------------------
# 2. Calculate team points
# -------------------------------

points = {}

for team in teams:
    points[team] = 0

# Scoring policy:
# Win = 3 points
# Draw = 1 point
# Loss = 0 points

for event, team1, team2, score1, score2 in results:

    if score1 > score2:
        points[team1] += 3

    elif score2 > score1:
        points[team2] += 3

    else:
        points[team1] += 1
        points[team2] += 1


# -------------------------------
# 3. Generate final rankings
# -------------------------------

ranking = sorted(
    teams,
    key=lambda team: points[team],
    reverse=True
)

print("\nFINAL RANKINGS")
print("--------------")

for rank, team in enumerate(ranking, start=1):
    print(rank, ".", team, "-", points[team], "points")
