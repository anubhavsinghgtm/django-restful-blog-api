from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost, Category, Tag

# Create your tests here.


class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        testCategory = Category.objects.create(name='html')
        testTag = Tag.objects.create(name='testing tag')
        testUser1 = User.objects.create_user(
            username='test_user1', 
            password='123456'
        )
        testPost = BlogPost.objects.create(
            title = 'Testing post 1',
            author_id = 1,
            body = 'Body of the testing post',
            published = True,
        )    

    def testBlogContent(self):
        post = BlogPost.postObject.get(id=1)
        cat = Category.objects.get(id=1)
        tag = Tag.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        published = f'{post.published}'
        
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Testing post 1')
        self.assertEqual(body, 'Body of the testing post')
        self.assertEqual(str(published), 'True')
        self.assertEqual(str(post), 'Testing post 1')
        self.assertEqual(str(cat), 'html')
        self.assertEqual(str(tag), 'testing tag')
