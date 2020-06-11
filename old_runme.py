from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager

chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--disable-gpu')
# chromeOptions.add_argument("window-size=768,1366")
chromeOptions.add_argument("--disable-dev-sha-usage")
chromeOptions.add_argument("--no-sandbox")

# driver_urls = []
# session_ids = []
drivers = []
uname_block = ['5arohisingh']
if drivers != []:
    pass
else:
    for i in uname_block:
        x = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        x.maximize_window()
        drivers.append(x)
        # driver_urls.append(x.command_executor._url)
        # session_ids.append(x.session_id)
        x.get("https://instagram.com")
        sleep(2)
        try:
            x.find_element_by_link_text("Follow").click()
        except (NoSuchElementException or ElementClickInterceptedException):
            sleep(1)
            x.find_element_by_link_text("Follow").click()
        sleep(2)
        x.find_element_by_name("username").send_keys(i)
        x.find_element_by_name("password").send_keys("Kartik@777")
        sleep(2)
        try:
            x.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div/div/div[1]/div/form/div[4]/button') \
                .click()
        except NoSuchElementException:
            x.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div') \
                .click()
        sleep(2)
        j = 0
        try:
            if j == 0:
                captcha_present = x.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div[2]/div/div/div[2]/div/button')
                print("Captcha Locked For " + i)
                x.close()
        except NoSuchElementException:
            print("Logged In With " + i)
