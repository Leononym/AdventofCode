data = [line.rstrip() for line in open("day5_input")]
all_rows = [i for i in range(128)]
all_seats = [i for i in range(8)]
seat_ids = []
my_seat = None

# gets all seat positions
for seat in data:
    rows = all_rows
    seats = all_seats
    for i in range(7):
        if seat[i] == "F":
            rows = rows[:int(len(rows) / 2)]
        else:
            rows = rows[int(len(rows) / 2):]

    for i in range(7, 10):
        if seat[i] == "L":
            seats = seats[:int(len(seats) / 2)]
        else:
            seats = seats[int(len(seats) / 2):]

    seat_ids.append(rows[0] * 8 + seats[0])

# sorts seat in ascending order
sorted_seats = sorted(seat_ids)

# gets my_seat
for i in range(len(sorted_seats)):
    try:
        if sorted_seats[i] + 1 != sorted_seats[i+1]:
            my_seat = sorted_seats[i] + 1
    except IndexError:
        pass

print(f"Highest seat number: {sorted_seats[len(sorted_seats)-1]}\nMy seat: {my_seat}")
