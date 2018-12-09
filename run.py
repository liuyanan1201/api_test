import unittest
from conf import config
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from lib.send_email import send_report
#测试加载器
#发现并收集用例得到一个测试集合
#遍历指定文件夹下及子包下的所有测试用例  test_
suite = unittest.defaultTestLoader.discover("./testcase")

#使用文本测试运行 运行这个测试集合
if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(suite)
    config.logging.info("测试开始"+"="*50)
    with open(config.report_file,"wb") as f:  #wb是二进制读写方式
        HTMLTestRunner(stream=f,title="user接口测试报告",description="测试报告").run(suite)

    if config.is_send_report:
        send_report()
        config.logging.info("发送成功")

    config.logging.info("测试结束"+"="*50)