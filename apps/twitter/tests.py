from django.test import TestCase
from django.urls import reverse

from apps.twitter.models import Tweet


class TweetTestCase(TestCase):
    def test_post_tweet(self):
        """Test tweet insertion through DRF endpoint"""
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

    def test_tweets_list(self):
        """Test list of tweets ordered by date of creation LIFO"""
        for i in range(1, 4):
            Tweet.objects.create(
                name=f'User {i}',
                message=f'Message from user {1}'
            )

        response = self.client.get(reverse('tweet-list'))
        self.assertEqual(200, response.status_code)

        result = response.json()
        names = [tweet['name'] for tweet in result]

        # Expect the same names in reverse order
        expected = [f'User {i}' for i in reversed(range(1, 4))]
        self.assertEqual(expected, names)
