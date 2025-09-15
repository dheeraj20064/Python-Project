import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Enter the date in this format YYYY-MM-DD: ")
new_date = datetime.strptime(date, "%Y-%m-%d")
formatted_date = new_date.strftime("%Y-%m-%d")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{formatted_date}/", headers=header)
content = response.text

soup = BeautifulSoup(content, "html.parser")

# Get song titles and artists together
song_tags = soup.select("li.o-chart-results-list__item h3#title-of-a-story")
songs = []
artists = []

for tag in song_tags:
    title = tag.get_text(strip=True)
    artist_tag = tag.find_parent("li").select_one("span.c-label")
    if title and artist_tag:
        artist = artist_tag.get_text(strip=True)
        songs.append(title)
        artists.append(artist)

year = date.split("-")[0]

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="0eca5b0bd32049b2a9ab9cb34f348ac9",
    client_secret="0d48d8bf84024baa9792ec8c09e5905c",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt",
))

# Get current user's Spotify ID
user_id = sp.current_user()["id"]
song_uris = []

# Search each song with artist
for song, artist_name in zip(songs, artists):
    result = sp.search(q=f"track:{song} artist:{artist_name} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} by {artist_name} not found")

# Create playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{formatted_date} Billboard 100", public=False)

# Add songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"\n✅ Playlist created: {playlist['external_urls']['spotify']}")
print(f"🎶 {len(song_uris)} songs added.")
