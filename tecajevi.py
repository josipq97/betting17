from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from djangoProject import settings
from betting17.models import *

PATH = '/home/josip/projects/web_scraping/chromedriver'
URL = 'file:///home/josip/projects/rezultati_tecajevi_21.4.html'
driver = webdriver.Chrome(executable_path=PATH)
driver.get(URL)
try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//*[contains(@class, 'event__match')] | //*[contains(@class, 'event__header')]"))
    )
except:
    print('error')

date = driver.find_element_by_class_name('calendar__datepicker').text
data = []
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
        try:
            event['time'] = e.find_element_by_class_name('event__time').text
        except:
            event['time'] = 'Unknown'
        event['home'] = e.find_element_by_class_name('event__participant--home').text
        event['away'] = e.find_element_by_class_name('event__participant--away').text
        event['odds_1'] = e.find_element_by_class_name('event__odd--odd1').text
        event['odds_x'] = e.find_element_by_class_name('event__odd--odd2').text
        event['odds_2'] = e.find_element_by_class_name('event__odd--odd3').text
        matches_obj = Matches.objects.create(
            league_country=league_country,
            league_title=league_title,
            home=event['home'],
            away=event['away'],
            time=f'{event["time"]} {date}',
            odds_1=event['odds_1'],
            odds_x=event['odds_x'],
            odds_2=event['odds_2']
        )

driver.quit()

# Todo:
#   što ako nema koeficijenta za neku utakmicu
#   odvoji datum i vrijeme utakmice
