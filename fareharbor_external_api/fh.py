import requests
import os

api_app_key = os.environ['FAREHARBOR_API_APP_KEY']
api_user_key = os.environ['FAREHARBOR_API_USER_KEY']
r = requests.get("https://demo.fareharbor.com/api/external/v1/companies/?api-app=%s&api-user=%s" % (api_app_key, api_user_key))

print r.text
