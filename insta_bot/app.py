import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv ,dotenv_values


driver_path = os.path.join(os.path.curdir, "chromedriver.exe")

load_dotenv()

class InstaFollowerBot():
    def __init__(self, username=os.getenv("APP_USERNAME"), password=os.getenv("APP_PASSWORD"), driver_path=os.getenv("DRIVER_PATH")):
        self.username = username
        self.password = password
        self.driver_path = driver_path
        self.bot = webdriver.Chrome(str(driver_path))

    def login(self):
        self.bot.get('https://www.instagram.com/')
        try:
            username_field = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            login_btn = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button"))
            )
            password_field.send_keys(self.password)
            username_field.send_keys(self.username)
            login_btn.click()
            not_now_1 = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"))
            )
            not_now_1.click()
            not_now_2 = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[4]/div/div/div[3]/button[2]"))
            )
            not_now_2.click()
        except Exception as e:
            print(e)

    def search_user(self, username):
        search_bar = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input"))
        )
        search_bar.send_keys(username)
        search_bar.send_keys(Keys.RETURN)
        search_Result = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div"))
        )
        search_Result.find_elements_by_tag_name('a')[0].click()
        time.sleep(3)
        followers_list_link = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"))
        )
        followers_list_link.click()

        followers_list_box = WebDriverWait(self.bot, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[4]/div/div[2]/ul/div"))
        )

        for i in range(1, 5):
            self.bot.execute_script('window.scrollTo(0,document.body.scrollHeight)', followers_list_box)
            time.sleep(2)
        list_of_f = followers_list_box.find_elements_by_tag_name('li')
        for users in list_of_f:
            time.sleep(5)
            print(users.find_element_by_tag_name('a').text )
            users.find_element_by_tag_name('button').click()
            time.sleep(10)
            users.find_element_by_tag_name('button').click()
            confirm_unfollow = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[5]/div/div/div[3]/button[1]"))
            )
            time.sleep(2)
            confirm_unfollow.click()

    def exit(self):
        self.bot.quit()





bot = InstaFollowerBot()
bot.login()
dcoy = ['twerk', 'xxx', 'babes', 'porno', 'ariana', 'justin']
for i in dcoy:
    bot.search_user(i)
    time.sleep(10)
bot.exit()
