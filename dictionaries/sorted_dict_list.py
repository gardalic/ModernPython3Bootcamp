users = [
    {"username": "samuel", "tweets": [
        "I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []},
    {"tweets": ["dogs are the best", "I'm hungry"]}
]

# print(sorted(users, key=lambda user: user['username']))

# only name
# for user in sorted(users, key=lambda user: user['username']):
# print(user.get('username'))

# Comprehension try
print(
    [user.get('username') for user in sorted(users, key=lambda user: user.get('username', 'rand_user')) if user.get('username')])  # added if to escape None

# user.get('username') - generate list of names
# for user in sorted(users, key=lambda user: user.get('username', 'rand_user')) - generate list of sorted users by username
# if user.get('username') - remove None
