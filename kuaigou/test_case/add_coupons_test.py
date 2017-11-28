import os
import requests
import unittest
import sys
sys.path.append('/home/jane/p3_project/kuaigou/db_fixture')
from db_fixture import test_data

class AddCouponsTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://staging.wechat.kuaigou.co/index.php/Fuwu/ManageCoupon/submit.html'
        self.cookies = {'PHPSESSID':'qm82jggp1n1fcrb2g5hddqon50', 'nick_name':'admin', 'username':'admin'}


    def tearDown(self):
        print(self.result)


    def test_add_coupons_success(self):
        '''Add coupons success'''
        payload = {'coupon_name':'国庆节优惠券','method':1,'types':1,'face_value':10,'limit':50,'format':1,'object':1,'Citys':[234,2],'dateline_5':'2017-11-24','dateline_6':'2017-11-24','nums':10,'Receive':1,'dateline_7':'2017-11-24'}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.text

if __name__ == '__main__':
    test_data.init_datab()
    unittest.main()

