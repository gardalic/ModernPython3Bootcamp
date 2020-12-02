"""
    Write a function called make_song, which takes a count and a beverage, and returns a generator that yields verses 
    from a popular song about a the beverage. The number of verses in the song is determined by the count. 

    Each verse of the song should involve one fewer beverage, until there are no beverages remaining. (Check the examples 
    for details on the structure of the lyrics.) The default count should be 99, and the default beverage should be soda.
"""

'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(num=99, drink='soda'):
    song = range(num, -1, -1)
    for bottle in song:
        if bottle > 1:
            yield f"{bottle} bottles of {drink} on the wall."
        elif bottle == 1:
            yield f"Only 1 bottle of {drink} left!"
        else:
            yield f"No more {drink}!"


kombucha_song = make_song(5, "kombucha")
# print(next(kombucha_song))  # '5 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '4 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '3 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # '2 bottles of kombucha on the wall.'
# print(next(kombucha_song))  # 'Only 1 bottle of kombucha left!'
# print(next(kombucha_song))  # 'No more kombucha!'
# print(next(kombucha_song))  # StopIteration

default_song = make_song()
print(next(default_song))  # '99 bottles of soda on the wall.'
