from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

def main():
    driver.get('http://128.171.10.138:4000/units/general/honor_form/')

    # FILL IN YOUR INFORMATION BELOW

    first_name = 'FIRST NAME GOES HERE'
    last_name = 'LAST NAME GOES HERE'
    email = 'EMAIL GOES HERE'

    driver.find_element_by_id('c-0-5').send_keys(first_name)
    driver.find_element_by_id('c-1-4').send_keys(last_name)
    driver.find_element_by_id('c-2-3').send_keys(email)
    driver.find_element_by_id('c-submit-button').click()
    time.sleep(3)
    driver.close()

if __name__ == '__main__':
    main()
