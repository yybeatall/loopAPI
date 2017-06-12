import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from interface import globaldata



class AuthResetpwd(unittest.TestCase):
    ''' 登录 '''
    def setUp(self):
        self.base_url = "http://api.uc.loopcc.cn/auth/resetpwd"

    def tearDown(self):
        print(self.result)

    def test_auth_Resetpwd_all_null(self):
        ''' 所有参数为空 '''
        payload = {'username':'','password':'','token':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213006)
        self.assertEqual(self.result['error'], '未登录状态，服务不可用')

    def test_auth_Resetpwd_username_not_exist(self):
        ''' 用户名不存在 '''
        payload = {'username': 'who', 'password': '123456', 'token': globaldata.get_token()}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213007)
        self.assertEqual(self.result['error'], '未找到账号who')

    def test_auth_Resetpwd_password_not_exist(self):
        ''' 密码未填写 '''
        payload = {'username': 'yayatest', 'password': '', 'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 400410)
        self.assertEqual(self.result['error'], 'The {attribute} field is required.')

    def test_auth_Resetpwd_token_not_exist(self):
        ''' 未传token '''
        payload = {'username': 'yayatest', 'password': '123456', 'token': ''}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213006)
        self.assertEqual(self.result['error'], '未登录状态，服务不可用')

    def test_auth_Resetpwd_success(self):
        ''' 重置成功 '''
        payload = {'username': 'yayatest', 'password': '111111', 'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], True)




if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
