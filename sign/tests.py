# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
