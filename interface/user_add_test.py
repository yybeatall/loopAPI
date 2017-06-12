import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from interface import globaldata



class UserAdd(unittest.TestCase):
    ''' 登录 '''
    def setUp(self):
        self.base_url = "http://api.uc.loopcc.cn/user/add"

    def tearDown(self):
        print(self.result)

    def test_user_add_all_null(self):
        ''' 所有参数为空 '''
        payload = {'username':'','password':'','token':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213006)
        self.assertEqual(self.result['error'], '未登录状态，服务不可用')

    def test_user_add_username_not_set(self):
        ''' 用户名未设置 '''
        payload = {'username': '', 'password': '111111','token': globaldata.get_token()}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 500405)
        self.assertEqual(self.result['error'], 'loop.user.username')

    def test_user_add_password_not_set(self):
        ''' 密码未设置'''
        payload = {'username': 'yayatest2', 'password': '', 'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 500405)
        self.assertEqual(self.result['error'], 'loop.user.password')

    def test_user_add_username_exist(self):
        ''' 用户名已存在'''
        payload = {'username': 'yayatest', 'password': '111111', 'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        # TODO：抛错，返回码未知
        self.assertEqual(self.result['error_code'], 500405)
        self.assertEqual(self.result['error'], 'loop.user.password')

    def test_user_add_username_success(self):
        ''' 新增用户成功 '''
        payload = {'username': 'yayatest2', 'password': '111111', 'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['username'], 'yayatest2')



if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
