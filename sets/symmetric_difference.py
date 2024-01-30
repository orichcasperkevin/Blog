hours_of_day = list(range(1, 13))
person1_schedule = [1, 2, 5, 9, 10]
person2_schedule = [1, 2, 3, 4, 5]

# Convert schedules to sets
set_person1 = set(person1_schedule)
set_person2 = set(person2_schedule)

# Find the hours that either user has a meeting while the other doesnt
#free_hours_for_boardroom_meetings = set_person1 ^ set_person2 #caret op
#or 
free_hours_for_boardroom_meetings = set_person1.symmetric_difference(set_person2)

print("Free hours for using the boardroom:", sorted(free_hours_for_boardroom_meetings))