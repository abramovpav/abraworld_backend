from django.test import TestCase

# Create your tests here.

from  datetime import datetime, timedelta

from django.utils import timezone
from django.test import TestCase

from .models import Track


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = datetime.utcnow() + timedelta(days=30)
        future_question = Track(publish_at=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = datetime.utcnow() + timedelta(days=30)
        old_question = Track(publish_at=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = datetime.utcnow() - timedelta(hours=1)
        recent_question = Track(publish_at=time)
        self.assertEqual(recent_question.was_published_recently(), True)
