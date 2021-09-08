from rest_framework      import status
from rest_framework.test import APIClient, APITestCase

from accounts.models import User
from blogs.models    import Blog


class BlogAPITest(APITestCase):
    def setUp(self):
        user = User.objects.create_user(
            email    = 'testuser@naver.com',
            name     = 'testuser',
            password = 'test1111'
        )

        blog = Blog.objects.create(
            user  = user,
            title = 'testuser write 1',
            body  = 'testuser write 1'
        )

        user.save()
        blog.save()

        self.client.force_authenticate(user=user)

    def tearDown(self):
        User.objects.all().delete()
        Blog.objects.all().delete()
        
    
    def test_blog_list_success(self):
        client = APIClient()

        response = client.get('/api/blogs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_blog_create_success(self):
        
        data = {
            "user"  : 'user_id : 1',
            "title" : 'testuser write 1',
            "body"  : 'testuser write 1'
        }
        response = self.client.post('/api/blog/create/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
