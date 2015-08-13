# -*- encoding: utf-8 -*-
from django.db import models

import reversion

from base.model_utils import TimeStampedModel
from base.singleton import SingletonModel
from block.models import (
    Page,
    PageSection,
    Section,
)


