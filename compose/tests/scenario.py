# -*- encoding: utf-8 -*-
from block.models import (
    BlockError,
    Page,
    PageSection,
    Section,
    Url,
)
from cms.models import (
    Template,
    TemplateSection,
)
from compose.models import (
    Article,
    ArticleBlock,
    SECTION_BODY,
)
from compose.tests.model_maker import (
    make_article,
    make_article_block,
)


def get_article_content():
    result = Article.objects.all()
    if result:
        return result[0]
    else:
        raise BlockError("Cannot find any article content")


def get_page_home():
    return Page.objects.get(slug=Page.HOME)


def _init_article(block, title):
    """Create a main content section - if there isn't one already."""
    result = Article.objects.filter(block=block)
    if result:
        return result[0]
    else:
        print("make_article: {}".format(title))
        return make_article(block, 1, title)


def _init_article_block(page_section):
    try:
        result = ArticleBlock.objects.get(page_section=page_section)
    except ArticleBlock.DoesNotExist:
        print("make_article_block: {}".format(page_section))
        result = make_article_block(page_section)
    return result


def init_app_compose():
    home = Page.objects.init_page(
        Page.HOME,
        '',
        'Home',
        0,
        'compose/page_article.html',
        is_home=True,
    )
    # layout
    body = Section.objects.init_section(
        SECTION_BODY,
        SECTION_BODY.capitalize(),
        'compose',
        'Article',
        'compose.article.create',
    )
    PageSection.objects.init_page_section(home, body)
    # template
    template = Template.objects.init_template('compose/page_article.html')
    TemplateSection.objects.init_template_section(template, body)
    Url.objects.init_pages()
    # we wouldn't normally put protected views in the list of URLs
    Url.objects.init_reverse_url('Dashboard', 'project.dash')
    Url.objects.init_reverse_url('Settings', 'project.settings')
