from django.test import Client, TestCase
from foodCMS.models import NutritionInfo
from foodCMS.views import NutritionInfoListView

class NutritionInfoListViewTest(TestCase):
    def test_render_to_response(self):
        response = Client().get('/nutri-info-list/')
        self.assertEqual(response.status_code, 302)
        self.assertEquals(response.url,'/accounts/login/?next=/nutri-info-list/')
