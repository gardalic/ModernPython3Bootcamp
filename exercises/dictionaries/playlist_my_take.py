# My take on the playlist lession
# Model an ordered Spotify playlist. Songs have to have a title, artist and album

sp_playlist = [
    {
        "name": "Turn It Off",
        "artist": "Culture Abuse",
        "album": "Eating Hooks"
    },
    {
        "name": "New Dawn Fades",
        "artist": "Joy Division",
        "album": "Unknown Pleasures"
    },
    {
        "name": "Renata",
        "artist": "James Holden",
        "album": "The Inheritors"
    }
]

for song in sp_playlist:
    print(f"Song {sp_playlist.index(song) + 1}:")
    for k, v in song.items():
        print(f"\t{k}: {v}")
    
