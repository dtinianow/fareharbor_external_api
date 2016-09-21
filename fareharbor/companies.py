from fare_harbor_service import FareHarborService
from company import Company

class Companies(object):

    @classmethod
    def all(cls):
        raw_data = FareHarborService().get_companies()
        companies_data = raw_data['companies']
        return [ Company(i) for i in companies_data ]

    def find(self, shortname):
        companies = self.all()
        return next(company for company in companies if company.shortname == shortname)
