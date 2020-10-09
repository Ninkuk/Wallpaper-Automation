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
        key = json.load(f)["PEXELS_KEY"]

    random_choice = random.choice(queries)
    print("category: " + random_choice)

    params = dict(query=random_choice, per_page=random.randint(10, 80))
    endpoint = 'search'
    response = requests.get(
        'https://api.pexels.com/v1/' + endpoint,
        headers={
            'Authorization': key},
        params=params
    )

    response_json = response.json()
    print("per_page: " + str(response_json["per_page"]))
    return response_json


def sort_photos(photos):
    mobile, desktop, square = [], [], []

    for photo in photos:
        if photo["width"] > photo["height"]:
            desktop.append(photo)
        elif photo["width"] < photo["height"]:
            mobile.append(photo)
        else:
            square.append(photo)

    print("Mobile(" + str(len(mobile)) + ")", end=' | ')
    print("Square(" + str(len(square)) + ")", end=' | ')
    print("Desktop(" + str(len(desktop)) + ")")

    return mobile, desktop, square


def get_wallpapers(wallpapers):
    random.shuffle(wallpapers)
    random_wallpapers = random.choices(wallpapers, k=5)
    wallpaper = random.choice(random_wallpapers)

    home = str(Path.home())
    id = str(wallpaper["id"])
    url = wallpaper["src"]["original"]
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
    mobile, desktop, square = [], [], []

    while len(desktop) < 1:
        data = get_data()
        photos = data["photos"]
        mobile, desktop, square = sort_photos(photos)

    get_wallpapers(desktop)
    set_wallpaper()
    print()
