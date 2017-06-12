import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from interface import globaldata


class AuthChgpwd(unittest.TestCase):
    ''' 登录 '''
    def setUp(self):
        self.base_url = "http://api.uc.loopcc.cn/auth/chgpwd"

    def tearDown(self):
        print(self.result)

    def test_auth_chgpwd_all_null(self):
        ''' 所有参数为空 '''
        payload = {'oldpassword':'','newpassword':'','token':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213006)
        self.assertEqual(self.result['error'], '未登录状态，服务不可用')

    def test_auth_chgpwd_oldpassword_not_set(self):
        ''' 旧密码未填写 '''
        payload = {'oldpassword': '', 'newpassword': '123456', 'token': globaldata.get_token()}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213008)
        self.assertEqual(self.result['error'], 'No old password')

    def test_auth_chgpwd_oldpassword_error(self):
        ''' 旧密码不正确 '''
        payload = {'oldpassword': '1111117', 'newpassword': '123456', 'token': globaldata.get_token()}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213008)
        self.assertEqual(self.result['error'], 'No old password')

    def test_auth_chgpwd_newpassword_not_exist(self):
        ''' 新密码未填写 '''
        payload = {'oldpassword': '111111', 'newpassword': '', 'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 400410)
        self.assertEqual(self.result['error'], 'The {attribute} field is required.')

    def test_auth_chgpwd_token_not_exist(self):
        ''' token未传递 '''
        payload = {'oldpassword': '111111', 'newpassword': '123456', 'token': ''}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213006)
        self.assertEqual(self.result['error'], '未登录状态，服务不可用')

    def test_auth_chgpwd_success(self):
        ''' 密码修改成功 '''
        payload = {'oldpassword': '111111', 'newpassword': '123456', 'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], True)

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
