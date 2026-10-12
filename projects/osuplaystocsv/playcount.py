import requests

TOKEN = "your_access_token"
USER_ID = your_user_id

headers = {"Authorization": f"Bearer {TOKEN}"}

all_maps = []
offset = 0
limit = 100

while True:
    resp = requests.get(
        f"https://osu.ppy.sh/api/v2/users/{USER_ID}/beatmapsets/most_played",
        headers=headers,
        params={"limit": limit, "offset": offset}
    )
    batch = resp.json()
    
    if not batch:
        break
    
    all_maps.extend(batch)
    print(f"Fetched {len(all_maps)} so far...")
    offset += limit

print(f"Total: {len(all_maps)} maps")