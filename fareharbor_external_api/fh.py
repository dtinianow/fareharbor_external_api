import requests
import os

class Service:

    url = 'https://demo.fareharbor.com/api/external/v1/'
    api_app_key = os.environ['FAREHARBOR_API_APP_KEY']
    api_user_key = os.environ['FAREHARBOR_API_USER_KEY']
    payload = {'api-app': api_app_key, 'api-user': api_user_key}

    def get_companies(self):
        request = requests.get('%scompanies/' % self.url, params=self.payload)
        print request.text

    def get_items(self, shortname):
        request = requests.get('%scompanies/%s/items/' % (self.url, shortname), params=self.payload)
        print request.text

    def get_availabilities_by_date(self, shortname, data):
        request = requests.get('%scompanies/%s/items/%s/minimal/availabilities/date/%s/' % (self.url, shortname, data['pk'], data['date']), params=self.payload)
        print request.text

    def get_availabilities_by_date_range(self, shortname, data):
        request = requests.get('%scompanies/%s/items/%s/minimal/availabilities/date-range/%s/%s/' % (self.url, shortname, data[:pk], data[:start_date], data[:end_date]), params=self.payload)
        print request.text


x = Service()
# x.get_companies()
# x.get_items('bodyglove')
data = {'pk': 1108, 'date': '2016-11-14'}
# import code; code.interact(local=dict(globals(), **locals()))
x.get_availabilities_by_date('sharktourshawaii', data)
