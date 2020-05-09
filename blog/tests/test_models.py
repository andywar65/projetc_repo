from django.test import TestCase

from users.models import User
from streamblocks.models import IndexedParagraph
from blog.models import Article, UserUpload

class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        IndexedParagraph.objects.create()
        Article.objects.create(title='Article 1',
            date = '2020-05-09 15:53:00+02',
            stream = '[{"unique_id":"4h5dps","model_name":"IndexedParagraph","id":1,"options":{}}]')
        Article.objects.create(title='Article 2',
            date = '2020-05-09 15:58:00+02')
        User.objects.create(username='andywar65', password='P4s5W0r6')
        article = Article.objects.get(id = 1)
        user = User.objects.get(id = 1)
        UserUpload.objects.create(post=article, user=user, body='Foo Bar')

    def test_article_str_method(self):
        article = Article.objects.get(id = 1)
        self.assertEquals(article.__str__(), 'Article 1')

    def test_article_get_path(self):
        article = Article.objects.get(id = 1)
        self.assertEquals(article.get_path(), '/articoli/2020/05/09/article-1')

    def test_article_get_previous(self):
        article = Article.objects.get(id = 1)
        self.assertEquals(article.get_previous(), None)

    def test_article_get_next(self):
        article = Article.objects.get(id = 1)
        article_2 = Article.objects.get(id = 2)
        self.assertEquals(article.get_next(), article_2)

    def test_article_get_uploads(self):
        article = Article.objects.get(id = 1)
        uploads = UserUpload.objects.all()
        #workaround found in
        #https://stackoverflow.com/questions/17685023/how-do-i-test-django-querysets-are-equal
        self.assertQuerysetEqual(article.get_uploads(), uploads,
            transform=lambda x: x)
