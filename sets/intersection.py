# User interests
user1_interests = {'python', 'data science', 'machine learning'}
user2_interests = {'machine learning', 'deep learning', 'data engineering'}
user3_interests = {'python', 'web development', 'data science'}

# Find common interests among user1 and 3
#common_interests = user1_interests.intersection(user3_interests)
# or use the ampersand op 
common_interests = user1_interests & user3_interests

print("Common Interests:", common_interests)