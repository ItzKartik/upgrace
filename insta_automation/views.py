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

from insta_automation import runme
driver_urls = runme.driver_urls
session_ids = runme.session_ids
uname_block = runme.uname_block
# driver_urls = []
# uname_block = []
# session_ids = []


class Followers(View):
    template_name = 'index.html'

    def post(self, *args, **kwargs):
        username = self.request.POST['username']
        url = self.request.POST['url_1']
        self.username = username
        self.url = url
        u = models.used_by.objects.get(user=username)
        self.user = u
        #return HttpResponse("Done !!!")
        return self.give_driver_id()

    def give_driver_id(self):
        try:
            c = models.left_ids.objects.filter(link=self.user)
            d = (len(c) - 1)
            if d == -1:
                return HttpResponse("Our Insta ID's Outdated We Are Updating Them To Give You More")
            elif d == 0:
                left_username = c[0].username
                print(left_username)
            else:
                r = randint(0, d)
                left_username = c[r].username
                print(left_username)
        except ValueError:
            return HttpResponse("Please Try Again...")
        indexofid = 0
        for ids in uname_block:
            if left_username == ids:
                indexofid = uname_block.index(left_username)
        self.left_username = left_username
        self.indexofid = indexofid
        return self.follow_him()

    def follow_him(self):
        driver = webdriver.Remote(command_executor=driver_urls[self.indexofid], desired_capabilities={})
        driver.close()
        driver.session_id = session_ids[self.indexofid]
        driver.get(self.url)
        try:
            sleep(1)
            flw_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
            if flw_btn:
                flw_btn.click()
                print("Ipad_Mobile Followed")
        except (ElementClickInterceptedException, NoSuchElementException):
            try:
                flw_btn = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
                if flw_btn:
                    ActionChains(driver).move_to_element(flw_btn).click(flw_btn).perform()
                    print("PCFollowed")
            except (ElementClickInterceptedException, NoSuchElementException):
                try:
                    flw_btn = driver.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/header/section/div[1]/button')
                    if flw_btn:
                        sleep(0.2)
                        ActionChains(driver).move_to_element(flw_btn).click(flw_btn).perform()
                        print("Private Account Followed")
                except (ElementClickInterceptedException, NoSuchElementException):
                    try:
                        unflw_btn = driver.find_element_by_xpath(
                            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
                        if unflw_btn:
                            print("Account Already Followed")
                    except (ElementClickInterceptedException, NoSuchElementException):
                        return HttpResponse("Instagram Has Restrict Our Account Please Try Again...")
        models.left_ids.objects.get(link=self.user, username=self.left_username).delete()
        return HttpResponse("You Got 1 Genuine Followers")


def flw_count(request):
    if request.method == 'POST':
        user = request.POST['username']
        url = request.POST['url_1']
        try:
            models.used_by.objects.get(user=user)
        except ObjectDoesNotExist:
            u = models.used_by.objects.create(user=user)
            for i in models.insta_ids.objects.all():
                models.left_ids.objects.create(link=u, username=i.username)
        r = requests.get(url).text

        start = '"edge_followed_by":{"count":'
        end = '},"followed_by_viewer"'
        followers = r[r.find(start) + len(start):r.rfind(end)]

        return HttpResponse(followers)
    else:
        return HttpResponse("Something Went Wrong Check Your Username")


def mail_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['msg']

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        html = """
            <html>
              <head></head>
              <body>
                <h1>Hi Prince</h1>
                <p>You Just Got An Email From %s. Please Mail Him Back On %s.</p>
                <p>His Message Is : %s</p>
              </body>
            </html>
            """ % (name, email, message)
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.login('guptapz111@gmail.com', '(Kartik@737)')
        smtp_server.sendmail("guptapz111@gmail.com", 'itz.kartik7@gmail.com', msg.as_string())
        smtp_server.close()
        return redirect('index')
    else:
        e = 'Please Try Again Later...'
        pass
