# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from cms.tests.scenario import init_app_cms


class Command(BaseCommand):

    help = "Initialise 'cms' application"

    def handle(self, *args, **options):
        init_app_cms()
        print("Initialised 'cms' app...")
