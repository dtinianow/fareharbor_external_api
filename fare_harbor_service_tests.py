from fareharbor.fare_harbor_service import FareHarborService
import unittest


class FareHarborServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = FareHarborService()

    def test_gets_companies(self):
        self.assertEqual(self.service.get_companies(),
        {'companies': [{'shortname': 'bodyglove', 'name': 'Body Glove'}, {'shortname': 'islandsailing', 'name': 'Island Sailing'}, {'shortname': 'sharktourshawaii', 'name': 'North Shore Shark Adventures'}]})

    def test_gets_items(self):
        items = self.service.get_items('bodyglove')
        item_name = items[0]['name']
        self.assertEqual(item_name, 'Snorkel & Dolphin Adventure')

    def test_gets_lodgings(self):
        lodgings = self.service.get_lodgings('bodyglove')
        lodging_name = lodgings[0]['name']
        self.assertEqual(lodging_name, 'Alii Cove')

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(FareHarborServiceTest))
    return test_suite

mySuite = suite()

runner = unittest.TextTestRunner()
runner.run(mySuite)
