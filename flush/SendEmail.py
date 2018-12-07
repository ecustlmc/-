import smtplib
from email.header import Header
from email.mime.text import MIMEText
import ListBeauty
# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "18918632965"  # 用户名
mail_pass = "asd445566"  # 授权密码，非登录密码

sender = "18918632965@163.com"

def sendEmail(title,p,reciver):
    content = ListBeauty.ListBeauty(p)
    message = MIMEText(content, 'html', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join([reciver])
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, [reciver], message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    sendEmail("您的教务信息已经更新",["我是来自数162的李明辰","你好"],"631149514@qq.com")
    # receiver = '***'
    #send_email2(mail_host, mail_user, mail_pass, receiver, title, content)
