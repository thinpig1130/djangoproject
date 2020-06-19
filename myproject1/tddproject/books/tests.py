import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Book

# 테스트 케이스 하나. 테스트 케이스들은 class로 만들어 진다.
class BookMethodTests(TestCase):
    # 반드시 메소드 명을 test로 시작해야 한다.
    def test_recent_pub(self):
        """
        recent_publication() should return False for future publication dates.
        """
        futuredate = timezone.now().date() + datetime.timedelta(days=5)
        future_pub = Book(publication_date=futuredate)
        self.assertEqual(future_pub.recent_publication(), False)