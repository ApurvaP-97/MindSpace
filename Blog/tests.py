from django.test import TestCase

# Create your tests here.
from .models import Posts
from django.contrib.auth.models import User

class PostTestCase(TestCase):

	# Test case while passing Post.author as a string in dictionary format - Before User Instance was created
    # def setUp(self):
    #     Posts.objects.create(title="Test Title 1",content="Test content 1",author="Me")
    #     Posts.objects.create(title="Test Title 2",content="Test conent 2",author="Other")

    def setUp(self):
        Posts.objects.create(title="Test Title 1",content="Test content 1")
        Posts.objects.create(title="Test Title 2",content="Test content 2")

    def testPostAttributes(self):
        post1 = Posts.objects.get(title="Test Title 1")
        post2 = Posts.objects.get(content="Test content 2")
        self.assertEqual(post1.content, '"Test content 1"')
        self.assertEqual(post2.title, '"Test Title 2"')

    