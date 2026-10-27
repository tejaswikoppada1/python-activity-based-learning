### Python Program

# Hospital Resource Allocation and Capacity Monitoring

# Each ward contains:
# [Ward Name, Total Beds, Occupied Beds, Available Staff, Required Staff, Equipment Available]

wards = [
    ["Emergency", 20, 19, 4, 6, 2],
    ["ICU", 15, 14, 6, 8, 5],
    ["General", 40, 30, 8, 7, 10],
    ["Pediatrics", 25, 20, 4, 5, 6]
]

print("HOSPITAL RESOURCE MONITORING")
print("-----------------------------")

for ward in wards:

    name = ward[0]
    total_beds = ward[1]
    occupied_beds = ward[2]
    available_staff = ward[3]
    required_staff = ward[4]
    equipment = ward[5]

    available_beds = total_beds - occupied_beds

    print("\nWard:", name)
    print("Total Beds:", total_beds)
    print("Occupied Beds:", occupied_beds)
    print("Available Beds:", available_beds)
    print("Available Staff:", available_staff)
    print("Required Staff:", required_staff)
    print("Equipment Available:", equipment)

    # Check bed shortage
    if available_beds == 0:
        print("WARNING: No beds available!")
    elif available_beds <= 2:
        print("WARNING: Very few beds available.")

    # Check staff shortage
    if available_staff < required_staff:
        print("WARNING: Staff shortage!")
    else:
        print("Staff Status: Sufficient")

    # Check equipment
    if equipment <= 2:
        print("WARNING: Equipment shortage!")
    else:
        print("Equipment Status: Sufficient")


# Patient priority list
# [Patient Name, Severity Level]
# 1 = Critical, 2 = Serious, 3 = Normal

patients = [
    ["Patient A", 1],
    ["Patient B", 3],
    ["Patient C", 2],
    ["Patient D", 1],
    ["Patient E", 3]
]

# Sort patients according to priority
patients.sort(key=lambda patient: patient[1])

print("\n\nPATIENT PRIORITY")
print("----------------")

for patient in patients:

    name = patient[0]
    priority = patient[1]

    if priority == 1:
        status = "CRITICAL"
    elif priority == 2:
        status = "SERIOUS"
    else:
        status = "NORMAL"

    print(name, ":", status)
