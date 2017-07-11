# -*- coding: utf-8 -*-


from register.models import EmailVerifyRecord
from django.core.mail import send_mail
from nostray_prototype.settings import EMAIL_FROM


def random_str(randomlength=8):
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	if i in range(randomlength):
		str+=chars[random.randint(0, length)]
	return str


def emailVerify(email, send_type='registe'):
	email_record = EmailVerifyRecord()
	code = random_str(8)
	email_record.code = code
	email_record.email = email
	email_record.send_type = send_type
	email_record.save()

	email_title = ''
	email_body = ''

	if send_type == 'registe':
		email_title = '绑定邮箱链接'
		email_body = '请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)

		send_status = send_mail(email_title, email_body, EMAIL_FROM, [eamil])
		if send_status:
			pass