# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from cms.models import CodeSnippet


class Command(BaseCommand):

    help = "Initialise 'cms' demo data"

    def handle(self, *args, **options):
        snippet = 'body { color: purple; }'
        CodeSnippet.objects.create_code_snippet(CodeSnippet.CSS, snippet)
        print("Initialised 'cms' demo data...")
