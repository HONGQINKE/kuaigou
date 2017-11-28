import requests
import unittest
import sys
sys.path.append('/home/jane/p3_project/kuaigou/db_fixture')
from db_fixture import test_data

class AddRoleTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://staging.wechat.kuaigou.co/index.php/Fuwu/Sys/roleAdd.html'
        self.cookies = {'PHPSESSID':'0m6tskvnemti5iouib34cccak3', 'nick_name':'admin', 'username':'admin'}


    def tearDown(self):
        print(self.result)

    def test_add_role_null(self):
        '''参数为空'''
        payload = {'role_name':'','role_des':''}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.text
        self.assertIn('角色名称必须填写',self.result)


    def test_add_role_exist(self):
        '角色已存在'
        payload = {'role_name':'salesman','role_des':'remark'}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.text
        #self.result = r.json()
        self.assertIn('角色名称已经存在，请修改',self.result)
        #self.assertEqual(self.result['info'],'角色名称已经存在，请修改')

    def test_add_role_success(self):
        '''角色添加成功'''
        payload = {'role_name':'test11','role_des':'test11'}
        r = requests.post(self.url,data=payload,cookies=self.cookies)
        self.result = r.text
        self.assertIn('保存完成',self.result)


if __name__ == '__main__':
    test_data.init_data()
    unittest.main()

