# User interests
user1_interests = {'python', 'data science', 'machine learning'}
user2_interests = {'machine learning', 'deep learning', 'data engineering'}
user3_interests = {'python', 'web development', 'data science'}

# convert to sets
user1_interests_set,user2_interests_set,user3_interests_set  = set(user1_interests),set(user2_interests),set(user2_interests)

# Combine unique interests from all users
#all_interests = user1_interests.union(user2_interests, user3_interests)
# or use the pipe operatoe
all_interests = user1_interests | user2_interests | user3_interests

print("Combined Interests:", all_interests)