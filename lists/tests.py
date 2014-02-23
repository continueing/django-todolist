from django.core.urlresolvers import resolve
from django.http import HttpRequest, response
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page

# Create your tests here.



class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        home_page_path = 'home.html'
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string(home_page_path)
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        aResponse = home_page(request)

        self.assertIn('A new list item', aResponse.content.decode())

        expectedHtml = render_to_string('home.html', {'new_item_text': 'A new list item', })

        self.assertEqual(aResponse.content.decode(), expectedHtml)





