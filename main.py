from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

url = 'https://www.futurepedia.io/'
driver.get (url)

scroll_pause_time = 4  # Jeda antara setiap pengguliran
screen_height = driver.execute_script("return window.screen.height;")   # Tinggi layar browser
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
    elif i == 1000:
        break

hasil = []
a = 0
# Ambil data menggunakan BeautifulSoup setelah semua data terload
soup = BeautifulSoup(driver.page_source, "html.parser")
# Lakukan proses dan penyimpanan data sesuai kebutuhan Anda
contents = soup.findAll('div',{'class':'MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-4 css-12y6uts'})
for content in contents:
    name = content.findNext('h3',{'class':'MuiTypography-root MuiTypography-h6 MuiTypography-alignLeft css-nxqa8p'}).text
    link = content.findNext('div',{'class':'MuiBox-root css-8atqhb'})
    link = link.find('a')['href']

    a += 1
    #print(name)
    #print(link)
    result = {
        'Tool Name' : name,
        'Domain Name' : link
    }
    hasil.append(result)

df = pd.DataFrame(hasil)
df.to_csv('futurepedia.csv', index=False)
print(f'scroll sebanyak ',i, ' kali.')
print(f'data sebanyak ',a,' sudah diambil.')
print('file csv created')