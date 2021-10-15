import random
import wallpaper_unsplash
import wallpaper_pexels
import wallpaper_wsupercars
import datetime
import utils

if __name__ == '__main__':
    print(datetime.datetime.now())

    source = random.choice(['Pexels', 'Unsplash', 'WSupercars'])

    if source == 'Pexels':
        print('Pexels')
        mobile, desktop, square = [], [], []

        while len(desktop) < 1:
            data = wallpaper_pexels.get_data()
            photos = data["photos"]
            mobile, desktop, square = wallpaper_pexels.sort_photos(photos)

        wallpaper_pexels.get_wallpapers(desktop)
        utils.set_wallpaper()

    elif source == 'Unsplash':
        print('Unsplash')
        wallpaper_unsplash.get_wallpapers(wallpaper_unsplash.get_data())
        utils.set_wallpaper()

    elif source == 'WSupercars':
        print('WSupercars')
        wallpaper_wsupercars.get_wallpapers()
        utils.set_wallpaper()

    print()
