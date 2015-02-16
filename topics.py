
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
# enable browser logging
d = DesiredCapabilities.FIREFOX
d['loggingPrefs'] = {'browser': 'ALL'}
driver = webdriver.Firefox(capabilities=d)
# load some site
driver.get('http://localhost:3000')
# print messages
for entry in driver.get_log('browser'):
    print entry
 
print
 
driver.quit()
