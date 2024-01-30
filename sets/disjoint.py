# Employee attendance on Day 1
day1_attendees = ['Alice', 'Bob', 'Charlie', 'David']

# Employee attendance on Day 2
day2_attendees = ['David', 'Eva', 'Frank', 'Grace']

#convert to sets 
day1_attendees_set,day2_attendees_set = set(day1_attendees),set(day2_attendees)

# Check if the sets are disjoint
is_disjoint = day1_attendees_set.isdisjoint(day2_attendees_set)

# Display the result
if is_disjoint:
    print("No common attendees. Sets are disjoint.")
else:
    print("There are common attendees. Sets are not disjoint.")