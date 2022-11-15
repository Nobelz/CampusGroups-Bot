import argparse
import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

# Set up commandline arguments
help_text = "This selenium bot allows you to register for events on CampusGroups."

args_parser = argparse.ArgumentParser(description=help_text)
args_parser.add_argument('--time', '-t', help="set time to register at, formatted as hh:mm in military (24 hour) time")
args_parser.add_argument('--id', '-i', help="set id of registration ticket")
args_parser.add_argument('--url', '-u', help="set url of CampusGroups Event")
args_parser.add_argument('--number', '-n', help='set number of tickets to get (default is 1)')

args = args_parser.parse_args()
config = vars(args)

if args.time and args.id and args.url:
    ticket_id = int(config['id'])
    time = datetime.datetime.strptime(str(config['time']), '%H:%M')
    url = str(config['url'])
else:
    raise ValueError('Bro I need arguments man!')

if args.number:
    number = str(config['number'])
else:
    number = '1'

# Time to register at
registration_time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=time.hour, minute=time.minute,
                                                                                   second=1))
# Start the Selenium WebDriver
chromedriver_autoinstaller.install()
browser = webdriver.Chrome(service=Service())
browser.get(url)

print('Please sign in.')
input("Click ENTER after signing in.")

browser.get(url)

# Wait until it's time
while True:
    curr_time = datetime.datetime.now()
    time = "Waiting... " + curr_time.strftime('%H:%M:%S')
    print(time, end="\r")

    try:
        alert = browser.switch_to.alert
        alert.accept()
    except Exception:
        pass

    if curr_time >= registration_time:
        print("Refreshing...")
        break

browser.get(url)

WebDriverWait(browser, 100).until(lambda d: d.find_element(By.CLASS_NAME, 'btn-cg--event'))
WebDriverWait(browser, 100).until(lambda d: d.find_element(By.NAME, f'ticket_{ticket_id}'))

select_input = Select(browser.find_element(By.NAME, f'ticket_{ticket_id}'))
register_button = browser.find_element(By.CLASS_NAME, 'btn-cg--event')
select_input.select_by_visible_text(number)

register_button.click()

print('Success!')
input("Click ENTER to exit.")
