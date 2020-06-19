from django.test import TestCase

class SampleTestCase(TestCase):

        def test_index_url(self):
            response = self.client.get('/blog/')
            self.assertEqual(response.status_code, 200)
