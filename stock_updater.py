
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
import time
import os
#install imports with pip install, also download chromedriver for your chrome version
#the chromedriver.exe must be in the same direcotry as the script

url = "https://www.google.com/search?q=tesla+share&rlz=1C1DIMC_enFI868FI868&oq=tesla+share&aqs=chrome..69i57j0l7.2556j1j4&sourceid=chrome&ie=UTF-8"

class ShareScraper:
    def __init__(self, company_name,share_url):
        #headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver = os.getcwd() + "./chromedriver.exe"

        #settings
        self.company_name = company_name
        self.share_url = share_url
        self.bot = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        webdriver.chrome.options

    def stopBot(self):
        self.bot.quit()
    
    def check(self):
        bot = self.bot
        url = self.share_url
        name = self.company_name

        bot.get(url) #opens the given url

        #scrape the data
        sharePrice = bot.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span[1]').text
        #finds the elements from html via xpath, to use this open dev console and inspect element
        name = bot.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[1]/div[1]/div[1]').text
        print("Company name: " + name + " | Share price: " + sharePrice)

        #we need to parse the String of price to a float to be able to compare it
        converted_price =float(sharePrice.replace(',', '.'))
        print(converted_price)


        if (converted_price < 300):
            send_mail()

def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo
        
        #Edit in neccessary emails and application password for gmail account
        server.login('something@gmail.com', 'applicationpassword')
        subject = 'Price fell under purchase predetermined price'
        body = 'Check Tesla share price'
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            'loginemail@gmail.com',
            'recieveremail@anything.com',
            msg
        )
        print('Email has been sent!')
        server.quit()

bot = ShareScraper("Tesla", url)

bot.check()
time.sleep(5) #seconds
bot.stopBot() #close bot
