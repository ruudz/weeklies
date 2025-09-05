import os
import requests
import random
from dotenv import load_dotenv
from datetime import date

load_dotenv()
API_KEY = os.getenv("LASTFM_API_KEY")
USERNAME = os.getenv("LASTFM_USERNAME")
MAX_SUGGESTIONS = int(os.getenv("MAX_SUGGESTIONS", 20))
BASE_URL = "http://ws.audioscrobbler.com/2.0/"
PARAMS = f"&api_key={API_KEY}&format=json"
METHOD_WEEKLY_TRACK_CHART = "user.getweeklytrackchart"
METHOD_SIMILAR_TRACKS = "track.getsimilar"
METHOD_TOP_TRACKS = "user.gettoptracks"

def get_weekly_tracks():
    url = (
        f"{BASE_URL}"
        f"?method={METHOD_WEEKLY_TRACK_CHART}&user={USERNAME}{PARAMS}"
    )
    data = requests.get(url).json()
    tracks = [(t['artist']['#text'], t['name'])
              for t in data['weeklytrackchart']['track']]
    return tracks

def get_similar_tracks(artist, track):
    url = (
        f"{BASE_URL}"
        f"?method={METHOD_SIMILAR_TRACKS}&artist={requests.utils.quote(artist)}"
        f"&track={requests.utils.quote(track)}{PARAMS}"
    )
    data = requests.get(url).json()
    return [(s['artist']['name'], s['name'])
            for s in data.get('similartracks', {}).get('track', [])]

def get_all_tracks():
    page = 1
    all_tracks = set()
    while True:
        url = (
            f"{BASE_URL}"
            f"?method={METHOD_TOP_TRACKS}&user={USERNAME}{PARAMS}&limit=1000&page={page}"
        )
        data = requests.get(url).json()
        tracks = data.get('toptracks', {}).get('track', [])
        if not tracks:
            break
        for t in tracks:
            all_tracks.add((t['artist']['name'], t['name']))
        page += 1
    return all_tracks

def main():
    weekly_tracks = get_weekly_tracks()
    all_time_tracks = get_all_tracks()
    candidate_songs = set()

    for artist, track in weekly_tracks:
        similar = get_similar_tracks(artist, track)
        new_songs = [s for s in similar if s not in all_time_tracks]
        candidate_songs.update(new_songs)

    final_list = random.sample(list(candidate_songs), min(MAX_SUGGESTIONS, len(candidate_songs)))

    os.makedirs('suggestions', exist_ok=True)
    
    filename = os.path.join('suggestions', f"suggestions_{date.today().isoformat()}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        for artist, track in final_list:
            f.write(f"{artist} – {track}\n")

    print(f"Saved {len(final_list)} songs to {filename}")

if __name__ == "__main__":
    main()
