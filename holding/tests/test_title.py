# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from block.tests.helper import check_content_methods
from block.tests.scenario import default_moderate_state

from holding.tests.scenario import (
    get_title_content,
    init_app_holding,
)


class TestTitle(TestCase):

    def setUp(self):
        default_moderate_state()
        init_app_holding()

    def test_content_methods(self):
        c = get_title_content()
        check_content_methods(c, ignore_remove=True)
