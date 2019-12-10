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

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(username = 'test',password = 'testing123',is_student = True)

    def test_user_fields(self):
        user=User.objects.get(id=1)
        expected_user_name = f'{user.username}'
        self.assertEquals(expected_user_name, 'test')

class DomainModelTest(TestCase):
    def setUp(self):
        Domain.objects.create(name = 'SomeDomain',description = 'DomainInfo',domaintrack = "afamf")

    def test_domain_fields(self):
        d=Domain.objects.get(id=1)
        self.assertEquals(d.name,'SomeDomain')

