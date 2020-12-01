lst = [
    {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
    {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
    {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
]

for item in lst:
    if item['title'] == 'song2':
        item['new_key'] = 'test'

for elem in lst:
    print(elem)
