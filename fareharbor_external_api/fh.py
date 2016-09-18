import requests
import os

class Service:

    def __init__(self):
        api_app_key = os.environ['FAREHARBOR_API_APP_KEY']
        api_user_key = os.environ['FAREHARBOR_API_USER_KEY']
        self.request = requests.get("https://demo.fareharbor.com/api/external/v1/companies/?api-app=%s&api-user=%s" % (api_app_key, api_user_key))

    def get_companies(self):
        print self.request.text

x = Service()
x.get_companies()
