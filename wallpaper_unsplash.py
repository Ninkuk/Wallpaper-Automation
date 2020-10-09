from pathlib import Path
import glob
import os
import random
import requests
import datetime
import json

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

    home = str(Path.home())
    id = str(wallpaper["id"])
    url = wallpaper["urls"]["full"]
    print(id + ": " + url)
    file_name = home + '/Pictures/Wallpapers/wallpaper.jpeg'
    r = requests.get(url)
    with open(file_name, 'wb') as wall:
        wall.write(r.content)

def set_wallpaper():
    home = str(Path.home())
    file_name = home + '/Pictures/Wallpapers/wallpaper.jpeg'
    try:
        SCHEMA = "org.gnome.desktop.background"
        KEY = "picture-uri"
        gsettings = Gio.Settings.new(SCHEMA)
        gsettings.set_string(KEY, file_name)
    except:
        pass

if __name__ == '__main__':
    print(datetime.datetime.now())
    
    get_wallpapers(get_data())
    set_wallpaper()
    print()