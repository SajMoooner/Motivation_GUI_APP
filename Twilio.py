import smtplib
from email.message import EmailMessage
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
from random import random
from shareplum import Site
from shareplum import Office365

class Twilio(object):
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_sms(self, to_number, message):
        self.client.messages.create(
            to=to_number,
            from_=self.from_number,
            body=message
        )

class Motivation(object):
    def __init__(self):
        self.url = 'https://www.brainyquote.com/topics/motivation'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.quotes = self.soup.find_all('a', {'title': 'view quote'})

    def get_random_quote(self):
        return self.quotes[int(random() * len(self.quotes))].text

    def get_all_quotes(self):
        return self.quotes

class SendToEmail(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self, to_email, message):
        msg = EmailMessage()
        msg['Subject'] = 'Motivational Quote'
        msg['From'] = self.email
        msg['To'] = to_email
        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email, self.password)
            smtp.send_message(msg)

class CreateSharePointItem(object):
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def create_item(self, site_url, text,list_name='Motivation'):
            authcookie = Office365('SHAREPOINT_SITE', username=self.username,password=self.password).GetCookies()
            site = Site(site_url, authcookie=authcookie)
            sp_list = site.List(list_name)
            data = [{'Title': text},]
            sp_list.UpdateListItems(data=data, kind='New')






