import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#发送邮箱服务器
smtpserver = 'smtp.126.com'
user = 'weicundi2@126.com'
password = '123456'
sender = 'weicundi2@126.com'

receiver = '151849762@qq.com'
subject = 'python send email test'

#发送的附件
sendfile = open('D:\\log.txt', 'rb').read()

att = MIMEText(sendfile, 'base64', 'utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename = "log.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')   #1

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())  #1
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()