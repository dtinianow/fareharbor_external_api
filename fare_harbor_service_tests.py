from fareharbor.fare_harbor_service import FareHarborService
import unittest


class FareHarborServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = FareHarborService()

    def test_gets_companies(self):
        self.assertEqual(self.service.get_companies(),
        {'companies': [{'shortname': 'bodyglove', 'name': 'Body Glove'}, {'shortname': 'islandsailing', 'name': 'Island Sailing'}, {'shortname': 'sharktourshawaii', 'name': 'North Shore Shark Adventures'}]})

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(FareHarborServiceTest))
    return test_suite

mySuite = suite()

runner = unittest.TextTestRunner()
runner.run(mySuite)
