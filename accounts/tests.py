from rest_framework      import status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user  = User.objects.create_user(
            email    = "testuser@naver.com", 
            name     = "testuser", 
            password = "test1111",
        )
    
    def tearDown(self):
        User.objects.all().delete()

    def test_user_post_success(self):
        client = APIClient()
        
        user = {
            "email"     : "testuser2@naver.com",
            "name"      : "testuser2",
            "password"  : "test2222",
        }
        
        response = client.post('/user/signup/', user, format='json')
		
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_user_post_duplicated_name(self):
        client = APIClient()
        
        user = {
            "email"     : "testuser@naver.com",
            "name"      : "testuser",
            "password"  : "test",
        }
        
        response = client.post('/user/signup/', user, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authorkview_post_invalid_keys(self):
        client = APIClient()
        
        user = {
            "email"     : "testuser@naver.com",
            "name"      : "testuser",
            "password"  : "test",
            "gender"    : "man",
        }
        
        response = client.post('/user/signup/', user, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
