import os 
import unittest
import requests 

class AddCarTypeTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://staging.wechat.kuaigou.co/index.php/Fuwu/ManageCarModel/addCarModel.html'
        self.cookies = {'PHPSESSID':'0m6tskvnemti5iouib34cccak3', 'nick_name':'admin', 'username':'admin'}

 
    def tearDown(self):
        print(self.result)

    def test_add_car_type_success(self):
        payload = {'car_act':'add','carmodel_id':1,'carsize_id':1,'car_weight':4,'car_len':3,'car_height':2,'car_width':1,'img':'','car_attr':['乘客','搬运','拆座']}
        #session = requests.Session()
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        #self.result = r.text
        self.result = r.json()
        self.assertEqual(self.result['code'],'000000')
        self.assertEqual(self.result['message'],'保存成功')
        

if __name__ == '__main__':
    unittest.main()
