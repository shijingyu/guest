# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
from sign.models import Event,Guest
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 5T event", status=True, limit=2000, address='shenzhen', start_time='2017-10-20 22:00:00')
        Guest.objects.create(id=1, event_id=1,realname='alen', phone='123213213', email='alne@gmail.com',sign=False)

    def test_event_models(self):
        result = Event.objects.get(name="oneplus 5T event")
        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='123213213')
        self.assertEqual(result.realname, "alen")
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    def test_index_page_renders_index_template(self):
        #测试 index 登录首页
        response = self.client.get('/index/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')

class LoginActionTest(TestCase):

    def setUp(self):
        User.objects.create_user('admin','admin@mail.com','admin123456')

    def test_add_admin(self):
        #测试添加用户
        user = User.objects.get(username="admin")
        self.assertEqual(user.username,"admin")
        self.assertEqual(user.email, "admin@mail.com")

# class EventMangeTest(TestCase): 测试发布会
#
#     def setUp(self):
#         User.objects.create_user('admin','admin@mail.com','admin123456')
#         Event.objects.create(name="xiaomiMax",limit=2000,address='beijing',status=1,start_time='2017-8-10 12:30:00')
#         self.login_user=('username':'admin','password':'admin123456')
#
#     def test_event_mange_success(self):
#         respone = self.client.post('/login_action/',data=self.login_user)
#         respone = self.client.post('/event_manage')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"xiaomi5",respone.content)
#         self.assertIn(b"beijing",respone.content)

class SignIndexActionTest(TestCase):
    ''' 发布会签到 '''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        Event.objects.create(id=2, name="oneplus4", limit=2000, address='shenzhen', status=1, start_time='2017-6-10 12:30:00')
        Guest.objects.create(realname="alen", phone=18611001100, email='alen@mail.com', sign=0, event_id=1)
        Guest.objects.create(realname="una", phone=18611001101, email='una@mail.com', sign=1, event_id=2)
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)

    def test_sign_index_action_phone_null(self):
        ''' 手机号为空 '''
        response = self.client.post('/sign_index_action/1/', {"phone": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phone error.", response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        ''' 手机号或发布会id错误 '''
        response = self.client.post('/sign_index_action/2/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"event id or phone error.", response.content)

    def test_sign_index_action_user_sign_has(self):
        ''' 用户已签到 '''
        response = self.client.post('/sign_index_action/2/', {"phone": "18611001101"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"user has sign in.", response.content)

    def test_sign_index_action_sign_success(self):
        ''' 签到成功 '''
        response = self.client.post('/sign_index_action/1/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sign in success!", response.content)


# 运行所有用例：
# python3 manage.py test
#
# 运行sign应用下的所有用例：
# python3 manage.py test sign
#
# 运行sign应用下的tests.py文件用例：
# python3 manage.py test sign.tests
#
# 运行sign应用下的tests.py文件中的 GuestManageTest 测试类：
# python3 manage.py test sign.tests.GuestManageTest
