"""
Data Types: Strings and Numbers.
"""
# song1 = "213 seconds" #String.
# song2 = 213 #Number (Integer)
# song3 = 213.5 #Number (Float)

# song4 = "150"
# song5 = 250.25
# playlist = int(song4) + song5
# print(f"The playlist is {playlist} seconds")

"""
Converting Strings to Numbers.
"""
song1 = 200
song2 = 300
song3 = input("What is the length of the song? ")
song3_input = int(song3)
playlist = song1 + song2 + song3_input
print(f"The length of the playlist is {playlist} seconds.")
