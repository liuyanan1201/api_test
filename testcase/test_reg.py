import unittest

import requests
import json
from lib.db import check_user,del_user
from lib import load_data
from conf import config

# import db
class TestReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet=load_data.get_sheet(config.data_file,"注册")

    def test_reg_success(self):
        case_data=load_data.get_case(self.sheet,"test_reg_success")
        NAME="test100"
        if check_user(NAME):
            del_user(NAME)
        url =case_data[2]
        data=json.loads(case_data[3])
        excepted_res=json.loads(case_data[4])
        res=requests.post(url=url,json=data)
        self.assertDictEqual(excepted_res,res.json())

        #数据清理
        del_user("test100")

    def test_reg_wrong(self):
        url='http://115.28.108.130:5000/api/user/reg/'
        data={"name":"oo1","password":"123123"}
        res=requests.post(url=url,json=data)
        self.assertEqual(res.json()["msg"],"失败，用户已存在")
if __name__=="__main__":
    unittest.main(verbosity=2)

