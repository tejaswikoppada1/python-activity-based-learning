
# Nested Loop Examination Seating Generator

rows = 5
columns = 6
capacity = 30

# Reserved seats (row, column)
reserved = {(1, 3), (3, 5)}

student_number = 1
seat_count = 0

print("EXAMINATION SEATING ARRANGEMENT")
print("--------------------------------")

for row in range(1, rows + 1):

    for column in range(1, columns + 1):

        # Check classroom capacity
        if seat_count >= capacity:
            break

        # Create row and column identifier
        seat_id = f"R{row}C{column}"

        # Reserved position
        if (row, column) in reserved:
            print(f"{seat_id} : RESERVED", end="    ")

        # Alternate seating restriction
        elif (row + column) % 2 == 0:
            print(f"{seat_id} : EMPTY", end="    ")

        else:
            print(f"{seat_id} : Student {student_number}", end="    ")
            student_number += 1

        seat_count += 1

    print()
