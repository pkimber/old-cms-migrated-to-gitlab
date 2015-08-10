# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

import reversion

from block.models import (
    BlockModel,
    ContentModel,
    #LinkDocument,
    #LinkImage,
    Page,
)


SECTION_BODY = 'body'


class ArticleBlock(BlockModel):
    pass

reversion.register(ArticleBlock)


class Article(ContentModel):

    ARTICLE_TYPE_CHOICES = (
        ('text_left', 'Text Left'),
        ('text_right', 'Text Right'),
        ('text_only', 'Text Only'),
        ('picture_only', 'Picture Only'),
    )

    block = models.ForeignKey(ArticleBlock, related_name='content')
    order = models.IntegerField()

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='compose', blank=True)
    article_type = models.CharField(
        max_length=12,
        choices=ARTICLE_TYPE_CHOICES,
        default='text_left',
    )
    # this will keep the database cleaner and easier to understand
    # (better than using 'content_object')
    #link_image = models.ForeignKey(LinkImage, blank=True, null=True)
    #carousel = models.ManyToManyField(LinkImage)
    #link_document = models.ForeignKey(LinkDocument, blank=True, null=True)
    #link_url = models.ForeignKey(LinkUrl, blank=True, null=True)
    #link_page = models.ForeignKey(LinkPage, blank=True, null=True)

    #link = models.ForeignKey(Link, blank=True, null=True)
    #links = models.ManyToManyField(Links, blank=True, null=True)
    #image = models.ForeignKey(LinkImage, blank=True, null=True)
    # this would be a carousel or a list of images in the article
    #images = models.ManyToManyField(LinkImage, blank=True, null=True)

    #def get_link_url(self):
    #    if link_document:
    #        return link_document.url
    #    elif link_url:
    #        return link_url.url
    #    elif link_page:
    #        return link_page.url

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def url_publish(self):
        return reverse('compose.article.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.article.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.article.update', kwargs={'pk': self.pk})

reversion.register(Article)


class FeatureBlock(BlockModel):
    pass

reversion.register(FeatureBlock)


class FeatureStyle(models.Model):
    """Select Feature CSS class """

    name = models.CharField(max_length=100)
    css_class_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Feature Style'
        verbose_name_plural = 'Feature Styles'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(FeatureStyle)


class Feature(ContentModel):
    """ Feature Block title, description (plain text), picture, URL and link type

    Used where we are providing a some links that we want to feature.

    """
    block = models.ForeignKey(FeatureBlock, related_name='content')
    order = models.IntegerField()

    title = models.TextField()
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='block', blank=True)
    url = models.URLField(blank=True, null=True)
    style = models.ForeignKey(FeatureStyle, blank=True, null=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Feature block'
        verbose_name_plural = 'Feature blocks'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    #def has_url(self):
    #    return True

    def set_url(self, url_link, url_text):
        self.url = url_link

    def get_url_link(self):
        return self.url

    def get_url_text(self):
        return None

    #def url_urledit(self):
    #  return reverse('compose.feature.urledit',
    #      kwargs={'pk': self.pk, 'block': 'Feature'})

    def url_publish(self):
        return reverse('compose.feature.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.feature.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.feature.update', kwargs={'pk': self.pk})

    def css_class_name(self):
        if self.style:
            return self.style.css_class_name
        else:
            return ''

reversion.register(Feature)


class HeaderStyle(models.Model):
    """Select Header CSS class """

    name = models.CharField(max_length=100)
    css_class_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Header style'
        verbose_name_plural = 'Header styles'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(HeaderStyle)


class HeaderBlock(BlockModel):
    pass

reversion.register(HeaderBlock)


class Header(ContentModel):
    """
    Header Block - title, description (rich text), picture and URL.
    Used for heading for a section.
    """
    block = models.ForeignKey(HeaderBlock, related_name='content')
    order = models.IntegerField()

    title = models.TextField()
    style = models.ForeignKey(HeaderStyle, blank=True, null=True)

    class Meta:
        # cannot put 'unique_together' on abstract base class
        # https://code.djangoproject.com/ticket/16732
        unique_together = ('block', 'moderate_state')
        verbose_name = 'Header'
        verbose_name_plural = 'Headers'

    def __str__(self):
        return '{} {}'.format(self.title, self.moderate_state)

    def url_publish(self):
        return reverse('compose.header.publish', kwargs={'pk': self.pk})

    def url_remove(self):
        return reverse('compose.header.remove', kwargs={'pk': self.pk})

    def url_update(self):
        return reverse('compose.header.update', kwargs={'pk': self.pk})

    def css_class_name(self):
        if self.style:
            return self.style.css_class_name
        else:
            return ''

reversion.register(Header)

class Menu (models.Model):
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    navigation = models.BooleanField(default=True)

    class Meta:
        ordering = ('navigation', 'slug',)
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return '{}'.format(self.title)

reversion.register(Menu)

class Link (models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=512)
    page = models.ForeignKey (Page, blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Link'

    def __str__(self):
        return '{} ({})'.format(self.title, self.url)

reversion.register(Link)


class MenuItem (models.Model):
    menu = models.ForeignKey(Menu, blank=False, null=True)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    link = models.ForeignKey (Link, blank=True, null=True)

    class Meta:
        ordering=('order','title',)
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return '{} - {}'.format(self.menu.title, self.title)

    def has_children(self):
        return bool(self.menuitem_set.count())

    def has_link(self):
        return bool(self.link)

    def get_link(self):
        if self.link:
            return self.link.url
        else:
            return '#'

reversion.register(MenuItem)


