# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import (
    TEST_PASSWORD,
    UserFactory,
)
from .factories import CodeSnippetFactory


class TestView(TestCase):

    def setUp(self):
        self.user = UserFactory(username='staff', is_staff=True)
        self.assertTrue(
            self.client.login(
                username=self.user.username,
                password=TEST_PASSWORD
            )
        )

    def test_code_snippet_list(self):
        url = reverse('cms.code.snippet.list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_code_snippet_create(self):
        url = reverse('cms.code.snippet.create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_code_snippet_update(self):
        snippet = CodeSnippetFactory()
        url = reverse('cms.code.snippet.update', args=[snippet.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_page_list(self):
        url = reverse('cms.page.list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
