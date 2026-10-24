### Python Program

# Smart Campus Incident and Maintenance Prioritization

# Report format:
# [Report ID, Problem, Severity, Location, Frequency]

reports = [
    [1, "Broken electrical wire", "High", "Laboratory", 5],
    [2, "Leaking tap", "Medium", "Canteen", 3],
    [3, "Broken chair", "Low", "Classroom", 2],
    [4, "Water leakage", "High", "Hostel", 6],
    [5, "Damaged road", "Medium", "Main Gate", 4],
    [6, "Faulty fan", "Low", "Classroom", 5]
]

# Severity scores
severity_score = {
    "High": 3,
    "Medium": 2,
    "Low": 1
}

# Location importance scores
location_score = {
    "Laboratory": 3,
    "Hostel": 3,
    "Main Gate": 2,
    "Canteen": 2,
    "Classroom": 1
}

# Calculate priority score
for report in reports:

    severity = report[2]
    location = report[3]
    frequency = report[4]

    report.append(
        severity_score[severity] +
        location_score[location] +
        frequency
    )

# Sort reports by priority score
reports.sort(key=lambda report: report[5], reverse=True)

print("SMART CAMPUS MAINTENANCE PRIORITY")
print("----------------------------------")

for rank, report in enumerate(reports, start=1):

    report_id = report[0]
    problem = report[1]
    severity = report[2]
    location = report[3]
    frequency = report[4]
    score = report[5]

    # Classify priority
    if score >= 10:
        priority = "URGENT"
    elif score >= 7:
        priority = "HIGH"
    elif score >= 5:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    print("\nRank:", rank)
    print("Report ID:", report_id)
    print("Problem:", problem)
    print("Severity:", severity)
    print("Location:", location)
    print("Reported Frequency:", frequency)
    print("Priority Score:", score)
    print("Priority:", priority)


# Priority summary
print("\n\nPRIORITY SUMMARY")
print("----------------")

urgent = 0
high = 0
medium = 0
low = 0

for report in reports:

    score = report[5]

    if score >= 10:
        urgent += 1
    elif score >= 7:
        high += 1
    elif score >= 5:
        medium += 1
    else:
        low += 1

print("Urgent Cases :", urgent)
print("High Cases   :", high)
print("Medium Cases :", medium)
print("Low Cases    :", low)
