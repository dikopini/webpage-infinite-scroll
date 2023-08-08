from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

def get_url():
    url = 'https://www.futuretools.io/'
    driver.get(url)
    scroll_pause_time = 3  # Jeda antara setiap pengguliran
    screen_height = driver.execute_script("return window.screen.height;")  # Tinggi layar browser
    i = 1
    while True:
        # Scroll ke bawah
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_pause_time)

        # Cek apakah sudah mencapai akhir halaman
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if screen_height * i > scroll_height:
            break
    print(f'scroll sebanyak ', i, ' kali.')


def get_content():
    soup = BeautifulSoup(driver.page_source, "html.parser")
    contents = soup.findAll('div', {'class':'tool w-dyn-item w-col w-col-6'})

    hasil = []
    a = 1
    for content in contents:
        isi = content.find('div',{'class':'tool-item-text-link-block---new'})
        name = isi.text
        link = isi.find('a',{'class':'tool-item-new-window---new w-inline-block'})['href']
        a += 1
        result = {
            'Tool Name': name,
            'Domain Name': link
        }
        hasil.append(result)

    df = pd.DataFrame(hasil)
    df.to_csv('futuretools.csv', index=False)
    print(f'data sebanyak ', a, ' sudah diambil.')
    print('file csv created')


if __name__ == '__main__':
    get_url()
    get_content()