from requests_html import HTMLSession
import datetime
import random
import utils

def get_wallpaper_from_grid(session, url):
    request = session.get(url)
    request.html.render()
    
    wallpaper_holder = request.html.find('.wallpaper-holder', first=True)
    wallpaper_link = random.choice([link for link in wallpaper_holder.links if "1920 x 1080" in link])
    
    wallpaper_link = wallpaper_link[wallpaper_link.find('pic=') + 4:]
    print(wallpaper_link)
    
    utils.save_image(wallpaper_link)


def get_latest_wallpaper(session, url):
    url += 'wallpapers/regular-wallpapers/?sort=newest'
    get_wallpaper_from_grid(session, url)


def get_random_manufacturer(session, url):
    request = session.get(url)
    request.html.render()

    sidebar = request.html.find('.sidebar-left', first=True)
    manufacturer = random.choice(list(sidebar.links)).split('/')[-2]

    url += 'regularwallpapers/?category_name=' + manufacturer

    get_wallpaper_from_grid(session, url)


def get_top_ranked_wallpaper(session, url):
    rankings = ['most-popular-cars', 'fastest-accelerating-cars', 'highest-top-speeds', 'quickest-quarter-miles']

    request = session.get(url + random.choice(rankings))
    request.html.render()

    ranking_holder = request.html.find('.ranking-holder', first=True)
    car_page_url = random.choice(list(ranking_holder.links))

    get_wallpaper_from_grid(session, car_page_url)


def get_wallpapers():
    session = HTMLSession()
    url = 'https://www.wsupercars.com/'

    available_functions = [get_latest_wallpaper, get_random_manufacturer, get_top_ranked_wallpaper]
    random.choice(available_functions)(session, url)


if __name__ == '__main__':
    print(datetime.datetime.now())
    
    get_wallpapers()
    utils.set_wallpaper()