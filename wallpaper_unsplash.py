from pathlib import Path
import random
import requests
import datetime
import json
import utils

def get_data():
    with open('search-terms.txt') as f:
        queries = [line.rstrip('\n') for line in f]

    with open('credentials.json') as f:
        key = json.load(f)["UNSPLASH_KEY"]

    random_choice = random.choice(queries)
    print("category: " + random_choice)
    
    params = dict(query=random_choice, orientation='landscape')
    endpoint = '/photos/random'
    response = requests.get(
        'https://api.unsplash.com' + endpoint,
        headers={
            'Authorization': 'Client-ID ' + key},
        params=params
    )

    return response.json()

def get_wallpapers(wallpaper):
    id = str(wallpaper["id"])
    url = wallpaper["urls"]["full"]
    print(id + ": " + url)
    
    utils.save_image(url)

if __name__ == '__main__':
    print(datetime.datetime.now())
    
    get_wallpapers(get_data())
    utils.set_wallpaper()
    print()