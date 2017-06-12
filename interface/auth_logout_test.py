import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from interface import globaldata


class AuthLogout(unittest.TestCase):
    ''' 登录 '''
    def setUp(self):
        self.base_url = "http://api.uc.loopcc.cn/auth/logout"

    def tearDown(self):
        print(self.result)

    def test_auth_logout_all_null(self):
        ''' 所有参数为空 '''
        payload = {'token':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['error_code'], 213006)
        self.assertEqual(self.result['error'], '未登录状态，服务不可用')

    def test_auth_logout_success(self):
        ''' 密码修改成功 '''
        payload = {'token': globaldata.get_token()}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], True)

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
