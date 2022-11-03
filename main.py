import datetime
from time import sleep, time
import selenium
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.options import Options

from MyDriver import MyDriver
from datetime import datetime

# Getting the current date and time

# getting the timestamp

def try_and_repeat(fun, tries=10, sleep_time=1):
    for i in range(tries):
        try:
            fun()
            break
        except:
            sleep(sleep_time)
            continue

def click_element_with_waits(xpath_value):
    for i in range(3):
        try:
            driver.wait_until_element_will_be_visible(by=By.XPATH,
                                                      value=xpath_value)
            break
        except NoSuchElementException:
            continue
    element = driver.find_element(by=By.XPATH,
                                  value=xpath_value)
    try_and_repeat(element.click)


def scroll_down_page_till_element_will_be_visible(xpath_value):
    begin = time()


    while True:
        try:
            element = driver.find_element(by=By.XPATH,value=xpath_value)
            break
        except NoSuchElementException:
            if time() - begin > 10:
                raise TimeoutError("element not visible since " + str(10) + "s")
            html = driver.find_element(By.TAG_NAME,'html')
            html.send_keys(Keys.END)

options = Options()
options.add_argument("--headless")
#
# driver = MyDriver()
driver = MyDriver(options=options)

driver.get("https://info-car.pl/new/prawo-jazdy/sprawdz-wolny-termin/wybor-terminu")
sleep(3)
click_element_with_waits("/html/body/app-root/app-layout/app-accept-cookies/article/div/div[2]/ic-ghost-button/button")
my_account_button = driver.find_element(by=By.XPATH,
                                        value="/html/body/app-root/app-layout/app-header/div/div[4]/div[2]/div/span")
my_account_button.click()

driver.wait_until_element_will_be_visible(by=By.XPATH, value='//*[@id="username"]')
login_input = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
pass_input = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
login_input.send_keys("kaczatom4@gmail.com")
file = open("password","r")
pass_input.send_keys(file.readline())
file.close()
driver.find_element(by=By.XPATH, value='//*[@id="register-button"]').click()

click_element_with_waits("/html/body/app-root/app-layout/app-header/div/div[3]/a[1]/div[1]/div/i")

click_element_with_waits("/html/body/app-root/app-layout/app-header/div/div[3]/a[1]/div[2]/ul/a[1]/li/div")
# click_element_with_waits("/html/body/app-root/app-layout/app-header/div/div[3]/a[1]/div[2]/ul/a[1]/li/div")
click_element_with_waits(
    "/html/body/app-root/app-layout/app-service-category/section/div[2]/div/div[2]/app-subcategory/section/div/div/div/div[1]/div/a")

#
# click_element_with_waits('//*[@id="province"]')
# element = driver.find_element('//*[@id="province"]')
# element.send_keys("podkarpackie")
#
# click_element_with_waits('//*[@id="organization"]')
# element = driver.find_element('//*[@id="organization"]')
# element.send_keys("WORD Rzeszów")

while True:
    try:
        scroll_down_page_till_element_will_be_visible('//*[@id="province"]')
        click_element_with_waits('//*[@id="province"]')
        scroll_down_page_till_element_will_be_visible('//*[@id="podkarpackie"]')
        click_element_with_waits('//*[@id="podkarpackie"]')
        scroll_down_page_till_element_will_be_visible('//*[@id="organization"]')
        click_element_with_waits('//*[@id="organization"]')
        scroll_down_page_till_element_will_be_visible('//*[@id="word-rzeszów"]')
        click_element_with_waits('//*[@id="word-rzeszów"]')

        scroll_down_page_till_element_will_be_visible('//*[@id="category-select"]')
        click_element_with_waits('//*[@id="category-select"]')
        scroll_down_page_till_element_will_be_visible('//*[@id="a"]')
        click_element_with_waits('//*[@id="a"]')

        scroll_down_page_till_element_will_be_visible(        '/html/body/app-root/app-layout/app-check-exam-availability/div/main/app-exam-availability-exam-center-step/div/section[1]/div/ic-ghost-button/button')
        click_element_with_waits(        '/html/body/app-root/app-layout/app-check-exam-availability/div/main/app-exam-availability-exam-center-step/div/section[1]/div/ic-ghost-button/button')
        driver.execute_script("window.scrollTo(0, -10000)")


        scroll_down_page_till_element_will_be_visible("/html/body/app-root/app-layout/app-check-exam-availability/div/main/app-exam-availability-calendar-step/app-word-exam-calendar/div/form/div[1]/div[2]/input")
        click_element_with_waits("/html/body/app-root/app-layout/app-check-exam-availability/div/main/app-exam-availability-calendar-step/app-word-exam-calendar/div/form/div[1]/div[2]/input")

        # driver.execute_script("window.scrollTo(0, 500)")

        sleep(0.5)
        if "egzaminów spełniających wybrane kryteria" in driver.page_source:
            dt = datetime.now()
            print(f"{dt}: Nie ma nowych terminów")
            driver.refresh()
            sleep(1)

        else:
            print("JEEEEEEEEEEEEEEEEst termin")
            import smtplib, ssl

            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "kaczatom4@gmail.com"  # Enter your address
            receiver_email = "kaczatom4@gmail.com"  # Enter receiver address

            file = open("google_pas")
            password = file.readline()
            file.close()
            message = """JEST termin sprawdź infocar"""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password=password)
                server.sendmail(sender_email, receiver_email, message)
            exit(0)
            break
    except:
        print("try ")
        driver.get("https://info-car.pl/new/prawo-jazdy/sprawdz-wolny-termin/wybor-terminu")


# sprawdzenie czy była zmiana
# driver.get("file://C:\zzz\programing\infoCar_check\\test.html")
# while True:
#     if "piesek" in driver.page_source:
#         print("jest piesek")
#         sleep(1)
#         driver.refresh()
#     else:
#         "nie ma pieska"
#         print("nie ma pieska")
#         driver.close()
#         break
