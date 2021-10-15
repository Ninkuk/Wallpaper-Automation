from pathlib import Path
import ctypes
from sys import platform
import requests


def set_wallpaper():
    if platform == 'linux':
        set_linux_wallpaper()
    elif platform == 'win32':
        set_windows_wallpaper()
    else:
        print("This OS platform is not supported yet!")
        exit()


def set_linux_wallpaper():
    home = str(Path.home())
    file_name = home + '/Pictures/Wallpapers/wallpaper.jpeg'
    try:
        SCHEMA = "org.gnome.desktop.background"
        KEY = "picture-uri"
        gsettings = Gio.Settings.new(SCHEMA)
        gsettings.set_string(KEY, file_name)
    except:
        pass


def set_windows_wallpaper():
    home = str(Path.home())
    file_name = home + '\\Pictures\\Wallpapers\\wallpaper.jpeg'
    SPI_SETDESKWALLPAPER = 20
    try:
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, file_name, 0)
    except:
        pass


def save_image(url):
    home = str(Path.home())

    if platform == 'linux':
        file_name = home + '/Pictures/Wallpapers/wallpaper.jpeg'
    elif platform == 'win32':
        file_name = home + '\\Pictures\\Wallpapers\\wallpaper.jpeg'
    else:
        print("This OS platform is not supported yet!")
        exit()

    r = requests.get(url)
    with open(file_name, 'wb') as wall:
        wall.write(r.content)


if __name__ == '__main__':
    set_windows_wallpaper()
