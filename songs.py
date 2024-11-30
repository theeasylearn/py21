from ytmusicapi import YTMusic 
import webbrowser

print(dir(YTMusic))

yt = YTMusic()

song = input("enter song name : ")
result = yt.search(song,filter='songs')

# print(result[0])
song = result[0]
print(f"https://music.youtube.com/watch?v={song['videoId']}")

quary = f"https://music.youtube.com/watch?v={song['videoId']}"
print("song is ready....")
webbrowser.open(quary)
