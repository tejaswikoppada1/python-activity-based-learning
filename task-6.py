### Python Program


# Food Waste Monitoring System

acceptable_limit = 10   # Maximum acceptable wastage percentage

# Data:
# (Day, Meals Prepared, Meals Served)

days = [
    ("Monday", 100, 90),
    ("Tuesday", 120, 100),
    ("Wednesday", 150, 140),
    ("Thursday", 130, 105),
    ("Friday", 110, 95)
]

print("FOOD WASTE MONITORING SYSTEM")
print("-----------------------------")
print("Acceptable Wastage Limit:", acceptable_limit, "%")
print()

for day, prepared, served in days:

    # Calculate leftovers
    leftovers = prepared - served

    # Calculate wastage percentage
    wastage_percentage = (leftovers / prepared) * 100

    print(day)
    print("Meals Prepared :", prepared)
    print("Meals Served   :", served)
    print("Leftovers      :", leftovers)
    print("Wastage        :", round(wastage_percentage, 2), "%")

    # Check acceptable limit
    if wastage_percentage > acceptable_limit:
        print("STATUS         : EXCEEDS LIMIT")
    else:
        print("STATUS         : Within Limit")

    print()
