from selenium import webdriver
import random
import time
from selenium.common.exceptions import NoSuchElementException

class Bot:
    def __init__(self):

        wort1 = input("Wort, das angegeben weden soll:")
        wort = wort1
        chromedriverpfad = input("Pfad ihrer Chromedriver.exe Datei:")
        self.driver = webdriver.Chrome(chromedriverpfad)
        self.driver.get("https://www.surveymonkey.com/r/7JZRVLJ?embedded=1")
        time.sleep(2)
        main = True
        i = 0
        options = ["/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/select/option[2]",
                   "/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/select/option[3]",
                   "/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/select/option[4]",
                   "/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/select/option[5]"]

        while main:
            i += 1
            ran = random.randint(0, 3)
            self.driver.find_element_by_id("463803414").click()
            time.sleep(1.25
                       )
            self.driver.find_element_by_xpath(options[ran]).click()
            if i == 1:
                word = self.driver.find_element_by_xpath('//*[@id="463803684"]').send_keys(wort)
                time.sleep(1)
            if i == 1:
                self.driver.find_element_by_xpath(
                    "//*[@id='question-field-483089934']/fieldset/div/div/div/div/label/span[1]").click()

            try:
                self.driver.find_element_by_xpath("//*[@id='patas']/main/article/section/form/div[2]/button").click()
            except NoSuchElementException:
                time.sleep(1)
            try:
                self.driver.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button[1]').click()
            except NoSuchElementException:
                time.sleep(1)


larry = Bot()
