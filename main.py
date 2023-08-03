from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

url = 'https://www.futurepedia.io/'
driver.get (url)

scroll_pause_time = 2  # Jeda antara setiap pengguliran
screen_height = driver.execute_script("return window.screen.height;")   # Tinggi layar browser
i = 1
while True:
    # Scroll ke bawah
    driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
    i += 1
    time.sleep(scroll_pause_time)

    # Cek apakah sudah mencapai akhir halaman
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    #if screen_height * i > scroll_height:
    #    break
    if i == 20:
        break