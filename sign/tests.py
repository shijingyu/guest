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
