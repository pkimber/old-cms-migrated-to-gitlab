# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.tests.helper import check_content

from compose.tests.factories import HeaderFactory


class TestHeader(TestCase):

    def test_content_methods(self):
        c = HeaderFactory()
        check_content(c)
