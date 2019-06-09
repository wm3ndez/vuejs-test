from django.test import TestCase
from django.urls import reverse

from apps.twitter.models import Tweet


class TweetTestCase(TestCase):
    def test_post_tweet(self):
        data = {
            'name': 'john doe',
            'message': 'This is a test'
        }
        response = self.client.post(reverse('tweet-list'), data)
        self.assertEqual(201, response.status_code)

        result = response.json()
        self.assertEqual(data['name'], result['name'])
        self.assertEqual(data['message'], result['message'])
        self.assertEqual(1, Tweet.objects.count())
        print(result)
