# Comprehensive Smart Campus Management Simulation

students = [
    ["101", "Tejaswi", 85, 78, 90, 0],
    ["102", "Anjali", 92, 88, 84, 0],
    ["103", "Rahul", 75, 80, 70, 0]
]

events = []
resources = [
    ("Projector", 5),
    ("Laptop", 10),
    ("Smart Board", 4),
    ("Microphone", 6)
]

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Display Student Records")
    print("2. Calculate Attendance")
    print("3. Calculate Marks and Grade")
    print("4. Register for Event")
    print("5. Allocate Resources")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # 1. Student Records
    if choice == "1":
        print("\n--- Student Records ---")
        for student in students:
            roll, name, m1, m2, m3, attendance = student
            print("Roll No:", roll)
            print("Name:", name)
            print("Marks:", m1, m2, m3)
            print()

    # 2. Attendance
    elif choice == "2":
        print("\n--- Attendance ---")

        for student in students:
            roll, name, m1, m2, m3, attendance = student

            total_classes = int(input("Enter total classes for " + name + ": "))
            attended = int(input("Enter classes attended by " + name + ": "))

            attendance = (attended / total_classes) * 100
            student[5] = attendance

            if attendance >= 75:
                status = "Eligible"
            else:
                status = "Not Eligible"

            print(name, "Attendance:", round(attendance, 2), "%", status)

    # 3. Marks and Grade
    elif choice == "3":
        print("\n--- Marks and Grades ---")

        for student in students:
            roll, name, m1, m2, m3, attendance = student

            total = m1 + m2 + m3
            average = total / 3

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            else:
                grade = "D"

            print(name, "Total:", total,
                  "Average:", round(average, 2),
                  "Grade:", grade)

    # 4. Event Registration
    elif choice == "4":
        print("\n--- Event Registration ---")

        name = input("Enter student name: ")
        event = input("Enter event name: ")

        registration = (name, event)
        events.append(registration)

        print(name, "registered successfully for", event)

    # 5. Resource Allocation
    elif choice == "5":
        print("\n--- Resource Allocation ---")

        resource_name = input("Enter resource name: ")
        required = int(input("Enter required quantity: "))

        found = False

        for resource, available in resources:
            if resource.lower() == resource_name.lower():
                found = True

                if required <= available:
                    print(required, resource, "allocated successfully.")
                    print("Remaining:",
                          available - required)
                else:
                    print("Insufficient", resource, "available.")
                    print("Available quantity:", available)

        if not found:
            print("Resource not found.")

    # 6. Summary Report
    elif choice == "6":
        print("\n===== CAMPUS SUMMARY REPORT =====")

        print("Total Students:", len(students))
        print("Total Events Registered:", len(events))

        print("\nEvent Registrations:")
        if len(events) == 0:
            print("No registrations yet.")
        else:
            for name, event in events:       # Tuple unpacking
                print(name, "->", event)

        print("\nStudent Performance:")
        for student in students:
            roll, name, m1, m2, m3, attendance = student

            average = (m1 + m2 + m3) / 3

            if average >= 75:
                performance = "Good"
            else:
                performance = "Needs Improvement"

            print(name, "-", performance)

        print("\nAvailable Resources:")
        for resource, quantity in resources:  # Tuple unpacking
            print(resource, ":", quantity)

    # 7. Exit
    elif choice == "7":
        print("Thank you for using Smart Campus Management System!")
        break

    else:
        print("Invalid choice. Please try again.")