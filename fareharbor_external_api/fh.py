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
        request = requests.get('%scompanies/%s/items/%s/minimal/availabilities/date-range/%s/%s/' % (self.url, shortname, data['pk'], data['start_date'], data['end_date']), params=self.payload)
        print request.text

    def get_availability(self, shortname, pk):
        request = requests.get('%scompanies/%s/availabilities/%s/' % (self.url, shortname, pk), params=self.payload)
        print request.text

    def get_booking(self, shortname, uuid):
        request = requests.get('%scompanies/%s/bookings/%s/' % (self.url, shortname, uuid), params=self.payload)
        print request.text

    def get_lodgings(self, shortname):
        request = requests.get('%scompanies/%s/lodgings/' % (self.url, shortname), params=self.payload)
        print request.text

    def get_availability_lodgings(self, shortname, pk):
        request = requests.get('%scompanies/%s/availabilities/%s/lodgings/' % (self.url, shortname, pk), params=self.payload)
        print request.text
        
x = Service()

# x.get_companies()
# x.get_items('bodyglove')
# data_1 = {'pk': 1108, 'date': '2016-11-14'}
# x.get_availabilities_by_date('sharktourshawaii', data_1)
# data_2 = {'pk': 1108, 'start_date': '2016-11-14', 'end_date': '2016-11-17'}
# x.get_availabilities_by_date_range('sharktourshawaii', data_2)
# x.get_availability('bodyglove', 70050)
# x.get_booking('bodyglove', '85ab9e4c-03fd-4bd4-af67-4946aa426c79')
# x.get_lodgings('bodyglove')
# x.get_availability_lodgings('bodyglove', 70050)



# import code; code.interact(local=dict(globals(), **locals()))
