# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from block.models import Page, Section, PageSection
from cms.models import Template, TemplateSection
from compose.models import Link, Menu, MenuItem


class Command(BaseCommand):

    help = "Initialise 'compose' application"

    def handle(self, *args, **options):
        print ("Creating pages...")
        template_article = Template.objects.init_template('compose/page_article.html')
        template_feature = Template.objects.init_template('compose/page_feature.html')
        section_body = Section.objects.get(slug='body')
        section_header = Section.objects.init_section(
            'header',
            'HEADER',
            'compose',
            'Header',
            'compose.header.create',
        ) 
        section_feature = Section.objects.init_section(
            'feature',
            'FEATURE',
            'compose',
            'Feature',
            'compose.feature.create',
        ) 

        page_article = Page.objects.init_page(
            'article-demo',
            '',
            'Article Demo',
            0,
            'compose/page_article.html',
        )

        PageSection.objects.init_page_section(page_article, section_body)

        page_another = Page.objects.init_page(
            'another-page',
            '',
            'Another Page',
            0,
            'compose/page_article.html',
        )
        PageSection.objects.init_page_section(page_another, section_body)

        page_feature = Page.objects.init_page(
            'feature-demo',
            '',
            'Feature Demo',
            0,
            'compose/page_feature.html',
        )
        PageSection.objects.init_page_section(page_feature, section_header)
        PageSection.objects.init_page_section(page_feature, section_feature)

        page_header = Page.objects.init_page(
            'header-demo',
            '',
            'Header Demo',
            0,
            'compose/page_feature.html',
        )
        PageSection.objects.init_page_section(page_header, section_header)
        PageSection.objects.init_page_section(page_header, section_feature)

        page_first = Page.objects.init_page(
            'first-page',
            '',
            'First page',
            0,
            'compose/page_article.html',
        )

        PageSection.objects.init_page_section(page_first, section_body)



        print("Creating menu...")
        menu = Menu(slug='main', title='Main', navigation=True)
        menu.save()
        feature_link = Link(title='Feature Demo', url='/feature-demo/', page=page_feature)
        feature_link.save()
        header_link = Link(title='Header Demo', url='/header-demo/', page=page_header)
        header_link.save()
        article_link = Link(title='Article Demo', url='/article-demo/', page=page_article)
        article_link.save()
        another_link = Link(title='Another Page', url='/another-page/', page=page_another)
        another_link.save()

        dash_link = Link(title='Dashboard', url='/home/user/')
        dash_link.save()

        first_link = Link(title='First Page', url='/first-page/', page=page_first)
        first_link.save()

        menu_item = MenuItem(menu=menu, slug='demos', title='Demos', order=2)
        menu_item.save()
        sub_menu_item = MenuItem(
            menu=menu, slug='feature-demo', parent=menu_item,
            title='Feature Demo', order=1, link=feature_link
        )
        sub_menu_item.save()
        sub_menu_item = MenuItem(
            menu=menu, slug='header-demo', parent=menu_item,
            title='Header Demo', order=2, link=header_link
        )
        sub_menu_item.save()
        sub_menu_item = MenuItem(
            menu=menu, slug='article-demo', parent=menu_item,
            title='Article Demo', order=3, link=article_link
        )
        sub_menu_item.save()

        menu_item = MenuItem(menu=menu, slug='another-page',
            title='Another Page', order=3, link=another_link
        )
        menu_item.save()
        menu_item = MenuItem(menu=menu, slug='first-page',
            title='First Page', order=1, link=first_link
        )
        menu_item.save()

        menu_item = MenuItem(menu=menu, slug='dashboard',
            title='Dashboard', order=9, link=dash_link
        )
        menu_item.save()
        print("Menu created")
