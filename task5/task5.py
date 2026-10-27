### Python Program


# Bus Passenger Occupancy Simulation

capacity = 40
passengers = 0

# Data for each stop:
# (Stop Name, Boarding Passengers, Alighting Passengers)

stops = [
    ("Stop 1", 15, 0),
    ("Stop 2", 10, 3),
    ("Stop 3", 8, 5),
    ("Stop 4", 12, 2),
    ("Stop 5", 5, 10)
]

print("BUS PASSENGER OCCUPANCY SIMULATION")
print("-----------------------------------")
print("Bus Capacity:", capacity)
print()

for stop, boarding, alighting in stops:

    # Remove passengers who are getting off
    passengers -= alighting

    # Add passengers who are boarding
    passengers += boarding

    print(stop)
    print("  Boarding  :", boarding)
    print("  Alighting :", alighting)
    print("  Passengers:", passengers)

    # Check capacity
    if passengers > capacity:
        print("  STATUS    : CAPACITY VIOLATION!")
    else:
        print("  STATUS    : Within Capacity")

    print()
