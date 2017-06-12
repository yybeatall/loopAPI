import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from interface import globaldata



class AuthLogin(unittest.TestCase):
    ''' 登录 '''
    def setUp(self):
        self.base_url = "http://api.uc.loopcc.cn/auth/login"

    def tearDown(self):
        print(self.result)

    def test_auth_login_all_null(self):
        ''' 所有参数为空 '''
        payload = {'username':'','password':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 21349)
        self.assertEqual(self.result['error'], 'The {attribute} field is required.')

    def test_auth_login_username_not_exist(self):
        ''' 用户名不存在 '''
        payload = {'username': 'who', 'password': '123456'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 500)
        self.assertEqual(self.result['error'], 'Call to a member function getAuthIdentifier() on null')

    def test_auth_login_password_error(self):
        ''' 密码不正确 '''
        payload = {'username': 'admin', 'password': '12345'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213005)
        self.assertEqual(self.result['error'], '密码输入错误')

    def test_auth_login_success(self):
        ''' 登录成功 '''
        payload = {'username': 'yayatest', 'password': '111111'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['username'], 'yayatest')
        login_token = self.result['token']
        print(login_token)
        globaldata.set_token(login_token)
        t = globaldata.get_token()
        print(t)





if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
