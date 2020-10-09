import os
from random import getrandbits
import wallpaper_unsplash
import wallpaper_pexels
import datetime

if __name__ == '__main__':
    print(datetime.datetime.now())

    if getrandbits(1):
        print('Pexels')
        mobile, desktop, square = [], [], []

        while len(desktop) < 1:
            data = wallpaper_pexels.get_data()
            photos = data["photos"]
            mobile, desktop, square = wallpaper_pexels.sort_photos(photos)

        wallpaper_pexels.get_wallpapers(desktop)
        wallpaper_pexels.set_wallpaper()
    else:
        print('Unsplash')
        wallpaper_unsplash.get_wallpapers(wallpaper_unsplash.get_data())
        wallpaper_unsplash.set_wallpaper()

    print()
