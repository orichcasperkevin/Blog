hours_of_day = list(range(1, 13))
person1_schedule = [1, 2, 5, 9, 10]
person2_schedule = [1, 2, 3, 4, 5]

# Convert schedules to sets
set_person1 = set(person1_schedule)
set_person2 = set(person2_schedule)

# Find the hours that are free for both users
#free_hours_both_users = set(hours_of_day) - (set_person1 | set_person2)
# or 
free_hours_both_users = set(hours_of_day).difference(set_person1.union(set_person2))

print("Free hours for scheduling a meeting:", sorted(free_hours_both_users))
#Free hours for scheduling a meeting: [6, 7, 8, 11, 12]