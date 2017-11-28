import os
import requests
import unittest
import sys
sys.path.append('/home/jane/p3_project/kuaigou/db_fixture')
from db_fixture import test_data

class AddPriceTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://staging.wechat.kuaigou.co/index.php/Fuwu/ManagePrice/addPriceModel.html'
        self.cookies = {'PHPSESSID':'0m6tskvnemti5iouib34cccak3', 'nick_name':'admin', 'username':'admin'}


    def tearDown(self):
        print(self.result)

    
    def test_add_price_exists(self):
        '''Add exitsts price'''
        payload = {'region_id':234,'car_id':1,'car_start_mileage':25,'car_start_price':30,'car_beyond_mileage':1,'car_beyond_price':8,'act':'add'}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.json()
        self.assertEqual(self.result['code'],'000001')
        self.assertEqual(self.result['message'],'该车型的定价已经存在')

    def test_add_price_success(self):
        '''Add price success'''
        payload = {'region_id':2,'car_id':1,'car_start_mileage':22,'car_start_price':28,'car_beyond_mileage':1,'car_beyond_price':8,'act':'add'}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.json()
        self.assertEqual(self.result['code'],'000000')
        self.assertEqual(self.result['message'],'保存成功')

 



if __name__ == '__main__':
    test_data.init_data()
    unittest.main()

