import json

# from django.contrib.auth.models import User

from accounts.models import User
from django.urls import reverse
from rest_framework                  import response, status
from rest_framework.test             import APITestCase, APIClient


# class RegistrationTestCase(APITestCase):
#     def test_registration(self):
#         data = {
#             "email"     : "testuser@test.com",
#             "name"      : "testuser",
#             "password"  : "test1111",
#         }

#         response = self.client.post("/user/signup/", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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
        



    

 
    
    
    
    
    
    
    
    
    
    #   def api_authentication(self):
    #       self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
 
    #   def test_public_list_authenticated(self):
    #       response = self.client.get('/api/admins/')
    #       self.assertEqual(response.status_code, status.HTTP_200_OK)
    #       self.assertEqual(response.json(), [{'id':1, 'name':'한성봉', 'password':'1234', 'household_number':'2001', 'payment':'1000.000'}])
 
    #   def test_public_list_un_authenticated(self):
    #       self.client.force_authenticate(user=None)
    #       response = self.client.get('/api/admins/')
    #       self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)