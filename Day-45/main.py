import requests, json, re

res = requests.get("https://www.empireonline.com/movies/features/best-movies-2/", headers={"User-Agent": "Mozilla/5.0"})
data = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', res.text, re.DOTALL)
state = json.loads(data.group(1))

movies = state["listicle"]["items"]  # inspect this key path in the JSON
movie_list = [item["data"]["title"] for item in movies]

with open("movies.txt", "w", encoding="utf-8") as f:
    for m in movie_list:
        f.write(m + "\n")
print("Saved", len(movie_list), "movies")

