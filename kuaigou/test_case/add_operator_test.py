import os 
import requests
import unittest
import sys
sys.path.append('/home/jane/p3_project/kuaigou/db_fixture')
from db_fixture import test_data

class AddOperatorTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://staging.wechat.kuaigou.co/index.php/Fuwu/Sys/adminAdd.html'
        self.cookies = {'PHPSESSID':'0m6tskvnemti5iouib34cccak3', 'nick_name':'admin', 'username':'admin'}


    def tearDown(self):
        print(self.result)

    def test_add_operator_null(self):
        '''null parameters'''
        payload = {'user_name':'','user_nick_name':'','pwd':'','pwdCom':'','role_id':'','region_id':''}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.text
        self.assertIn('用户名必须填！',self.result)


    def test_add_operator_exists(self):
        '''Add exits operator'''
        payload = {'user_name':'admin','user_nick_name':'super admin','pwd':'123456','pwdCom':'123456','role_id':1,'region_id':234}
        r = requests.post(self.url,data=payload,cookies=self.cookies) 
        self.result = r.text
        self.assertIn('用户名已经存在！',self.result)

    def test_add_operator_success(self):
        '''Add operator success'''
        payload = {'user_name':'815653888@qq.com','user_nick_name':'elenan','pwd':'123456','pwdCom':'123456','role_id':1,'region_id':234}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.text
        self.assertIn('保存完成',self.result)

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()
