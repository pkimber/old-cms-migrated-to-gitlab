# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import (
    TEST_PASSWORD,
    UserFactory,
)

from block.tests.factories import (
    PageFactory,
    PageSectionFactory,
)
from compose.tests.factories import ArticleFactory


class TestView(TestCase):

    def setUp(self):
        self.user = UserFactory(username='staff', is_staff=True)
        self.assertTrue(
            self.client.login(
                username=self.user.username,
                password=TEST_PASSWORD
            )
        )

    def test_article_create(self):
        p = PageSectionFactory(page=PageFactory(slug_menu=''))
        url = reverse(
            'compose.article.create',
            kwargs=dict(
                page=p.page.slug,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'pkimber.net',
                'article_type': 'text_only',
                'image_size': '1-3',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_article_create_page_and_menu(self):
        p = PageSectionFactory()
        url = reverse(
            'compose.article.create',
            kwargs=dict(
                page=p.page.slug,
                menu=p.page.slug_menu,
                section=p.section.slug,
            )
        )
        response = self.client.post(
            url,
            {
                'title': 'pkimber.net',
                'article_type': 'text_only',
                'image_size': '1-4',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_article_publish(self):
        c = ArticleFactory()
        response = self.client.post(
            reverse('compose.article.publish', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)

    def test_article_update(self):
        c = ArticleFactory()
        response = self.client.post(
            reverse('compose.article.update', kwargs={'pk': c.pk}),
            {
                'title': 'pkimber.net',
                'article_type': 'text_only',
                'image_size': '1-2',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_article_remove(self):
        c = ArticleFactory()
        response = self.client.post(
            reverse('compose.article.remove', kwargs={'pk': c.pk}),
        )
        self.assertEqual(response.status_code, 302)
