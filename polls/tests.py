# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
from django.test import TestCase, Client

from models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_the_index_view(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 404)
