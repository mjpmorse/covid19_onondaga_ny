##############################################################
#                                                            #
#   Routine for scraping Onondaga County's dashboard to      #
#   construct a covid19 time series by municipalities        #
#                                                            #
# Author:  Michael J. P. Morse                               #
# License: file 'LICENSE.txt'                                #
# Date: 04/04/2020                                           #
#                                                            #
##############################################################


import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from selenium import webdriver
from datetime import datetime


# Load the Onondaga dashboard
my_url = ('https://socpa.maps.arcgis.com/apps/'
          'opsdashboard/index.html#/7bd218bc8be04b209c0b80a83fc2eba5')
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

driver.get(my_url)
p_elements = driver.find_elements_by_class_name("external-html")

p_elements_date = \
    driver.find_element_by_class_name(('subtitle.text-ellipsis'
                                       '.no-pointer-events.margin-right-half'))
todays_cases = {}

for element in p_elements:
    split = element.text.split(":")
    municipalities = split[0].strip()
# Update 04/06. Onondaga changed dashboard. New line to make code work again.
    cases = split[1].strip().split(" ")[0]
    cases = int(cases)
    todays_cases[municipalities] = cases

month = p_elements_date.text.split(' ')[2]
day = p_elements_date.text.split(' ')[3].split(',')[0]
last_update_dt = datetime.strptime("".join([day, '/', month]), "%d/%B")
last_update = datetime.strftime(last_update_dt, '%m/%d')

# make a dateframe out of todays cases
df_today = pd.DataFrame(todays_cases.values(), index=todays_cases.keys())
df_today.rename(columns={0: last_update}, inplace=True)

# close the webdriver_manager
driver.quit()

df_time_series = pd.read_csv('onondaga_time_series.csv', index_col=0)
df_time_series[last_update] = df_today[last_update]
df_time_series.to_csv(r'onondaga_time_series.csv', index=True)
