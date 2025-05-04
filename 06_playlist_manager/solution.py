# do not change the method name
def main():
    # Empty playlist
    playlist = []

    print("Welcome to Playlist Manager!\n")
    
    # Add songs
    print("Adding: 'Bohemian Rhapsody - Queen'")
    playlist.append("Bohemian Rhapsody - Queen")
    print(f"Current playlist: {playlist}\n")

    print("Adding: 'Hotel California - Eagles'")
    playlist.append("Hotel California - Eagles")
    print(f"Current playlist: {playlist}\n")

    print("Adding: 'Sweet Child O'Mine - Guns N'Roses'")
    playlist.append("Sweet Child O'Mine - Guns N'Roses")
    print(f"Current playlist: {playlist}\n")

    print("Adding: 'Billie Jean - Michael Jackson'")
    playlist.append("Billie Jean - Michael Jackson")
    print(f"Current playlist: {playlist}\n")

    print("Adding: 'Stairway to Heaven - Led Zeppelin'")
    playlist.append("Stairway to Heaven - Led Zeppelin")
    print(f"Current playlist: {playlist}\n")

    # Show last 3 added songs
    print(f"Recently added songs (last 3): {playlist[-3:]}\n")

    # Show first and last songs
    print(f"First song: {playlist[0]}")
    print(f"Last song: {playlist[-1]}\n")

    # Remove 2 songs
    playlist.remove("Hotel California - Eagles")
    playlist.remove("Sweet Child O'Mine - Guns N'Roses")
    print(f"Current playlist after removal: {playlist}\n")

    # Add one more song
    print("Adding: 'Imagine - John Lennon'")
    playlist.append("Imagine - John Lennon")
    print(f"Updated playlist: {playlist}\n")

    # Show top 2 songs
    print(f"Top songs: {playlist[:2]}")

# Do not change the following lines:
main()
