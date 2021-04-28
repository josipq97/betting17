import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, time
from djangoProject import settings
from betting17.models import *


def format_date(dt):
    dt = dt.text.split()[0].split('/')
    dt = datetime.date(2021, int(dt[1]), int(dt[0]))
    return dt


def format_time(tm):
    if 'SKR' in tm:
        tm = tm.replace('\nSKR', '')
    tm = tm.split(':')
    tm = datetime.time(int(tm[0]), int(tm[1]))
    return tm


PATH = '/home/josip/projects/web_scraping/chromedriver'
URL = 'file:///home/josip/projects/rezultati_29_4.html'
driver = webdriver.Chrome(executable_path=PATH)
driver.get(URL)
try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//*[contains(@class, 'event__match')] | //*[contains(@class, 'event__header')]"))
    )
except:
    print('error')

event_date = format_date(driver.find_element_by_class_name('calendar__datepicker'))
print(event_date)
league_country = ''
league_title = ''

for e in elements:
    if 'event__header' in e.get_attribute('class'):
        league_country = e.find_element_by_class_name('event__title--type').text
        league_title = e.find_element_by_class_name('event__title--name').text
    if 'event__match' in e.get_attribute('class'):
        event = {}
        event['league_country'] = league_country
        event['league_name'] = league_title
        event['date'] = date
        event['home'] = e.find_element_by_class_name('event__participant--home').text
        event['away'] = e.find_element_by_class_name('event__participant--away').text
        event['odds_1'] = e.find_element_by_class_name('event__odd--odd1').text
        event['odds_x'] = e.find_element_by_class_name('event__odd--odd2').text
        event['odds_2'] = e.find_element_by_class_name('event__odd--odd3').text
        try:
            event['time'] = format_time(e.find_element_by_class_name('event__time').text)
            # event['time'] = e.find_element_by_class_name('event__time').text
        except:
            event['time'] = '-'
        print(event)

        if event['odds_1'] is not '-' and event['time'] is not '-':
            matches_obj = Matches.objects.create(
                league_country=league_country,
                league_title=league_title,
                home=event['home'],
                away=event['away'],
                date=event_date,
                time=f'{event["time"]} {date}',
                odds_1=event['odds_1'],
                odds_x=event['odds_x'],
                odds_2=event['odds_2']
            )
driver.quit()

# Todo:
#   što ako nema koeficijenta za neku utakmicu
#   odvoji datum i vrijeme utakmice
