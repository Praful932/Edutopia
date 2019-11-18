from django.test import TestCase
from django.urls import reverse,resolve
from app.views import index
from app.models import User,Domain,Student,Mentor,Post

class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url=reverse('index')
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_index_resolves_index(self):
        view=resolve('/')
        self.assertEquals(view.func,index)