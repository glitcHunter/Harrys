from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_hpme_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
		
    def test_home_page_returns_correct_html(self):
        ''' Sprawdzamy czy po wysłaniu żądania do home_page zobaczymy (otrzymamy odpowiedź) <title> lista</title>
        zacząwszy od <html> i kończywszy </html>'''

        request = HttpRequest() # obiekt request
        response = home_page(request) # przesłanie żądania do widoku home_page

        self.assertTrue(response.content.startswith(b'<html>'))#
        self.assertIn(b'<title>lista</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))