import requests
import os

class Service:

    url = 'https://demo.fareharbor.com/api/external/v1/'
    api_app_key = os.environ['FAREHARBOR_API_APP_KEY']
    api_user_key = os.environ['FAREHARBOR_API_USER_KEY']
    payload = {'api-app': api_app_key, 'api-user': api_user_key}

    def get_companies(self):
        request = requests.get("%scompanies/?api-app=%s&api-user=%s" % (self.url, self.api_app_key, self.api_user_key))
        print request.text

x = Service()
x.get_companies()
