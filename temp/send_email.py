#1、组装邮件正文
#2、组装邮件头
#3、连接smtp服务器并发送邮件

import smtplib #连接smtp服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#组装邮件正文
msg = MIMEMultipart()
body = MIMEText('python发送的邮件','plain','utf-8') #plain是纯文字 还可以是html
msg.attach(body)
#组装邮件头
msg['From'] = 'liuyn120731@126.com'
msg['To'] = '694526779@qq.com'
msg["Subject"] = "from python"


#4、附件
with open("../report/report.html","rb") as f:
    att_file = f.read()

att=MIMEText(att_file,'base64','utf-8')
att["Content-Type"]="application/octet-stream"#声明附件的内容格式MIME数据流格式
att["Content-Disposition"]="attachment;filename='report.html'"#附件描述信息 filename是附件显示的文件名
msg.attach(att)

#连接smtp服务器并发送
smtp = smtplib.SMTP_SSL("smtp.126.com")
smtp.login("liuyn120731@126.com","liuyanan123")
smtp.sendmail("liuyn120731@126.com",
              "694526779@qq.com",
              msg.as_string())#将MIME格式邮件转成字符串发送


