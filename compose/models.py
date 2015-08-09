# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

import reversion

from block.models import (
    BlockModel,
    ContentModel,
    Image,
    Link,
)


SECTION_BODY = 'body'


class ArticleBlock(BlockModel):
    """Move to ``cms`` (not ``compose``)."""
    pass

reversion.register(ArticleBlock)


class Article(ContentModel):
    """Move to ``cms`` (not ``compose``)."""

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
    #picture = models.ImageField(upload_to='compose', blank=True)
    article_type = models.CharField(
        max_length=12,
        choices=ARTICLE_TYPE_CHOICES,
        default='text_left',
    )
    # link wizard fields
    link = models.ForeignKey(
        Link,
        related_name='article_link',
        blank=True, null=True
    )
    references = models.ManyToManyField(Link)
    picture = models.ForeignKey(
        Image,
        related_name='picture',
        blank=True, null=True
    )
    # this would be a carousel or a list of images in the article
    carousel = models.ManyToManyField(Image)

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

    @property
    def wizard_fields(self):
        return {
            'carousel': Image.MULTI,
            'link': Link.SINGLE,
            'picture': Image.SINGLE,
            'references': Link.MULTI,
        }


reversion.register(Article)


class FeatureBlock(BlockModel):
    """Move to ``cms`` (not ``compose``)."""
    pass

reversion.register(FeatureBlock)


class FeatureStyle(models.Model):
    """Select Feature CSS class.

    Move to ``cms`` (not ``compose``).

    """

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
    """Feature Block title, description (plain text), picture, URL and link
    type

    Used where we are providing a some links that we want to feature.

    Move to ``cms`` (not ``compose``).

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
    """Select Header CSS class.

    Move to ``cms`` (not ``compose``).

    """
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
    """Move to ``cms`` (not ``compose``)."""
    pass

reversion.register(HeaderBlock)


class Header(ContentModel):
    """
    Header Block - title, description (rich text), picture and URL.
    Used for heading for a section.

    Move to ``cms`` (not ``compose``).

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
