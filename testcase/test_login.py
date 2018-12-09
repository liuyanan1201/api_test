import unittest
import json
import requests
from lib import load_data
from lib import case_log
from lib import case_log
from conf import config
#声明一个测试类 继承unittest.TestCase
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   #整个测试只执行一次  是测试准备方法
        cls.sheet = load_data.get_sheet(config.data_file,"登录")
    # @unittest.skip()#无条件跳过
    # @unittest.skipUnless("跳过该测试用例")  #跳过该条用例  不满足条件时跳过
    # @unittest.skipIf(not check_user("张三"),"跳过该测试用例") #满足条件时跳过  当张三不存在时跳过
    def test_login_normal(self):    #测试正常登录
        case_data = load_data.get_case(self.sheet,"test_login_normal")
        url=case_data[2]
        data=json.loads(case_data[3])
        res=requests.post(url=url,data=data)
        case_log.log_case_info("test_login_normal",url,case_data[3],case_data[4],res.text)
        self.assertEqual(res.text,"<h1>登录成功</h1>")#断言相等  判断两个字符串是否相等

    def test_login_password_wrong(self):   #测试密码错误登录
        case_data = load_data.get_case(self.sheet,"test_login_password_wrong")
        url=case_data[2]
        data=json.loads(case_data[3])
        res=requests.post(url=url,data=data)
        case_log.log_case_info("test_login_password_wrong",url,case_data[3],case_data[4],res.text)
        self.assertIn("<h1>失败，用户名或密码错误</h1>",res.text)



if __name__=="__main__":
    unittest.main(verbosity=2)#可以指定显示级别
