import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = #Amazon product url
headers = {"User-Agent": #user agent}

def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find('span', {'class': 'a-price-whole'}).get_text()
    converted_price = float(price.replace('.', '').replace(',','').strip())

    if converted_price < 3500:
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(#sender email ID , #app password)

    subject = 'Price fell down!'
    body = 'Check out the Amazon link' + url
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(#receiver email ID, #receiver email ID, msg)
    print('Email sent!')
    server.quit()

while (True):
    check_price()
    time.sleep(86400)
    # Repeats each day
