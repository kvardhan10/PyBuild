
# importing Flask and other modules
from flask import *
from datetime import date
import requests
from bs4 import BeautifulSoup

# Flask constructor
app = Flask(__name__, template_folder='templates')

#list of days
day = { 1 : "today",
        2 : "yesterday",
        3 : "tomorrow",
        4 : "weekly",
        5 : "monthly",
        6 : "CUSTOM DATE"}

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def get_input():
    if request.method == "POST":
       sign = request.form.get("hs")
       time = request.form.get("time")
       result = horoscope(sign,time)
       return result
    return render_template('index.html')

def horoscope(sign, date):
    if (int(date) < 4):
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day[int(date)]}.aspx?sign={sign}")
    elif(int(date) > 3 and int(date) < 6):
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-{day[int(date)]}.aspx?sign={sign}")
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
        res = item.p.text
    return res

if __name__=='__main__':
   app.run()
