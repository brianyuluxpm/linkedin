from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput import keyboard
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import io
import time
from selenium.webdriver.chrome.options import Options


class linkedin:
    def __init__(self):
        pass

    def linkedin(self, chromePath, companyList, username, password):
        url = 'https://www.linkedin.com/'
        r = requests.get(url)
        r.cookies
        chromePath = str(chromePath)
        company = str(companyList)
        headers = { 'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'en-US,en;q=0.8',
            'Cache-Control':'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
        }

        for key, value in enumerate(headers):
            capability_key = 'phantomjs.page.customHeaders.{}'.format(key)
            webdriver.DesiredCapabilities.PHANTOMJS[capability_key] = value
        opts = Options()
        opts.add_argument("user-agent=whatever you want")
        wd = webdriver.Chrome(chromePath, chrome_options=opts)



        wd.get('https://www.linkedin.com/login')
        id = str(username)
        password = str(password)

        wd.maximize_window()
        wd.implicitly_wait(10)
        un = wd.find_element_by_id('username')
        pw = wd.find_element_by_id('password')
        un.send_keys(id)
        pw.send_keys(password)
        wd.find_element_by_class_name("login__form_action_container ").click()
        time.sleep(10)

        with open(company) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                linkName = line.strip()
                br = False
                for page in range(1, 5):
                    time.sleep(1)
                    speed = 1000
                    try:
                        wd.get(
                            'https://www.linkedin.com/sales/search/people?companyIncluded=' + str(linkName) + '&companyTimeScope=CURRENT&doFetchHeroCard=false&geoIncluded=103644278%2C101174742&logHistory=true&page=' + str(page) +'&searchSessionId=DqBvzmcETWGIobTHZdj5Fw%3D%3D&titleIncluded=CEO%2CCIO%2CCTO%2CProject%2520Manager%3A4%2CProject%2520Engineer%3A78%2CEngineering%2520Manager%3A174%2CVice%2520President%2520Of%2520Engineering%3A520%2CSenior%2520Engineering%2520Manager%3A1358%2CSoftware%2520Engineering%2520Manager%3A1685%2CHead%2520Of%2520Engineering%3A1945&titleTimeScope=CURRENT')
                        time.sleep(1)


                        for who in range(0, 5):
                            wd.execute_script("window.scrollTo(0," + str(speed) + ")")
                            speed = speed + 1000
                            print(speed)

                        wd.implicitly_wait(10)


                        element = wd.find_elements_by_xpath("//button[@class='result-lockup__connect button--unstyled full-width text-align-left']")
                        if not element:
                            break
                        else:
                            for l in element:
                                wd.implicitly_wait(10)
                                wd.execute_script("arguments[0].click();", l)
                                wd.implicitly_wait(10)
                                wd.find_element_by_xpath("(//button[@class='button-primary-medium connect-cta-form__send'])").click()
                                wd.implicitly_wait(10)
                                try:
                                    wd.find_element_by_xpath(
                                        "(//li-icon[@type='cancel-icon'])").click()
                                except:
                                    pass
                        if len(element) < 1:
                            break
                        else:
                            pass



                    except:
                        pass


                line = fp.readline()
                cnt += 1

if __name__ == '__main__':
    username = "" #include your id in quotation marks
    password = "" #include the passwords in quotation marks
    chromePath = "" #download chromeDriver and indicate its path here
    companyList = "" #where is the group text file?
    linkedin.linkedin(chromePath, companyList, username, password)






