# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from compose.tests.scenario import init_app_compose


class Command(BaseCommand):

    help = "Initialise 'compose' application"

    def handle(self, *args, **options):
        init_app_compose()
        print("Initialised 'compose' app...")
