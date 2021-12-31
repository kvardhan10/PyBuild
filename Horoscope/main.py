from datetime import date
import requests
from bs4 import BeautifulSoup

#list of zodiac sign
zodiac_sign = {  "Aries": 1,
    "Taurus": 2,
    "Gemini": 3,
    "Cancer": 4,
    "Leo": 5,
    "Virgo": 6,
    "Libra": 7,
    "Scorpio": 8,
    "Sagittarius": 9,
    "Capricorn": 10,
    "Aquarius": 11,
    "Pisces": 12 }

#list of days
day = { 1 : "today",
        2 : "yesterday",
        3 : "tomorrow",
        4 : "weekly",
        5 : "monthly",
        6 : "CUSTOM DATE"}

#scraping function
def get_horoscope_by_day(zodiac_sign: int, day: str, d: int):
    if (d < 4):
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    elif(d > 3 and d < 6):
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-{day}.aspx?sign={zodiac_sign}")
    else:
        year = input("Enter year: ")
        month = input("Enter month: ")
        date_user = input("Enter date: ")
        custom = (year + month + date_user)
        today = date.today()
        d1 = today.strftime("%Y%m%d")
        if (custom < d1):
            res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={custom}")
        else:
            print('Date exceeded from today.')
            exit(0)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.findAll('div', {'class': 'main-horoscope'})
    for item in data:
        print(item.p.text)

print(zodiac_sign)
z = str(input("Choose your zodiac sign: "))
print(day)
d = int(input("Choose Horoscope type: "))
get_horoscope_by_day(zodiac_sign[z],day[d],d)
