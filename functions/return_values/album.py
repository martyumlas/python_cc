def make_album(artist, album):
    return {
        'artist': artist,
        'album': album
    }

# print(make_album('eraserheads', 'circus'))
# print(make_album('riverymaya', 'rivermaya'))

while True:
    print('enter q anytime to quit')

    artist = input('Enter artist: ')
    if artist == 'q':
        break
    album = input('Enter album: ')
    if album == 'q':
        break

    print(make_album(artist, album))

