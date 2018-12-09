import unittest
from testcase import test_login,test_reg
smoke_suite = unittest.TestSuite()
smoke_suite.addTest(test_login.TestLogin("test_login_normal"))
smoke_suite.addTest(test_reg.TestReg("test_reg_success"))


# all=unittest.defaultTestLoader.discover(".")

if __name__=="__main__":
    unittest.TextTestRunner(verbosity=2).run(smoke_suite)