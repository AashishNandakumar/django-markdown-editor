from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title='My title', description='blub', wiki='post body')
        self.assertEqual(post.title, 'My title')
        self.assertEqual(post.description, 'blub')
        self.assertEqual(post.wiki, 'post body')
