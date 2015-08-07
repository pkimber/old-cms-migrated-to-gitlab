# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

import reversion

from block.models import (
    BlockModel,
    ContentModel,
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

    IMAGE_SIZE = (
        ('1-2', 'Half Width'),
        ('1-3', 'Third Width'),
        ('1-4', 'Quarter Width'),
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
    image_size = models.CharField(
        max_length=3,
        choices=IMAGE_SIZE,
        default='1-2',
    )

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
