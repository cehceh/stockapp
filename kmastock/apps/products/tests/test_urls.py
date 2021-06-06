from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import add_product, edit_product
# from apps.products.views import add_product, edit_product


class TestUrls(SimpleTestCase):

    def test_add_product_url_resolves(self):
        url = reverse('products:add_product')
        print(resolve(url).func, add_product)
        # self.assertEquals(resolve(url).func, add_product)
        # self.assertEquals(resolve(url).func, add_product)
        
        # https://stackoverflow.com/questions/60230504/django-url-unit-test-comparison-of-expected-view-function-fails
        f = resolve(url).func
        self.assertEqual(f.__name__, add_product.__name__)
        self.assertEqual(f.__module__, add_product.__module__)
