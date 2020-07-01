from selenium.webdriver.support.ui import WebDriverWait
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, redirect
from selenium import webdriver
from time import sleep
from insta_automation import models
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import requests
from django.views.generic import View
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui

from insta_automation import runme
# driver_urls = runme.driver_urls
# session_ids = runme.session_ids


# driver_urls = []
# uname_block = []
# session_ids = []
# uname_block = ['5arohisingh']

# uname = [
#             'kalmesh.gpt123',
#             'paryan456',
#             'banajiajay',
#             'akshaysharma9537',
#             'ruhilohariwal',
#             'sritesh009',
#             'abhinashtudu',
#             'harishagarwal90',
#             'azadaslam7',
#             '5arohisingh',
#             'dhirajsaho',
#             'ankit95678',
#             'keshulohariwal',
#             'gulabosaho',
#             '3aceboyz',
#             'aman.gpt876',
#             'rohit.sharma737',
#             'taniya.mirja656',
#             'niraj.saw939'
#         ]


class icommenter(View):
    template_name = 'index.html'

    def post(self, *args, **kwargs):
        take_this_username = self.request.POST['take_this_username']
        url = self.request.POST['url_1']
        commented_txt = self.request.POST['comment']
        self.take_this_username = take_this_username
        self.commented_txt = commented_txt
        self.url = url
        print("here")
        return HttpResponse("Done...")
        # return self.give_driver_id()

    def give_driver_id(self):
        drivers = runme.drivers
        self.drivers = drivers
        uname_block = runme.uname_block
        # try:
        #     d = (len(uname_block) - 1)
        #     if d == -1:
        #         return HttpResponse("Our Insta ID's Outdated We Are Updating Them To Give You More")
        #     elif d == 0:
        #         left_username = uname_block[0]
        #         print(left_username)
        #     else:
        #         r = randint(0, d)
        #         left_username = uname_block[r]
        #         print(left_username)
        # except ValueError:
        #     return HttpResponse("Please Try Again...")
        indexofid = 0
        for ids in uname_block:
            if take_this_username == ids:
                indexofid = uname_block.index(take_this_username)
        self.indexofid = indexofid
        return self.commentit()

    def commentit(self):
        driver = self.drivers
        driver.get(self.url)
        sleep(1)
        comment = ''
        if self.commented_txt is None:
            comments = ['Cool Man', 'Awesome']
            comment = comments[randint(0, 1)]
        else:
            comment = self.commented_txt
        ctextarea = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea')))
        ActionChains(driver).move_to_element(ctextarea).click(ctextarea).send_keys(comment).send_keys(Keys.ENTER).perform()
        return HttpResponse("Your Post Just Got Commented")
