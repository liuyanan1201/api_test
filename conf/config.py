

#数据库配置

db_host='115.28.108.130'
db_port=3306
db_user='test'
db_password='123456'
db='api_test'


#路径配置
import os
# __name__当前模块名
# __file__当前文件
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path=os.path.join(project_path,'data')#数据文件目录
data_file=os.path.join(project_path,'data','data.xls')

#日志文件根目录
log_file = os.path.join(project_path,'log','log.txt')
report_file = os.path.join(project_path,'report','report.html')


#log配置
import logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a"
                    )

if __name__ == "__main__":
    # logging.info("hello,world")
    # logging.info("中文日志")
    print(project_path)
    print(data_path)
    print(data_file)
    print(log_file)
    print(report_file)


#邮件配置
smtp_server = "smtp.126.com"
smtp_user = "liuyn120731@126.com"
smtp_password = "liuyanan123"

receiver = "694526779@qq.com"
subject = "接口测试报告"
body = "hi,all,\n附件中是接口测试报告请查收。"

is_send_report = False #不发送邮件










