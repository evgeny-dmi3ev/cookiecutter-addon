# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _


@python_2_unicode_compatible
class {{ cookiecutter.project_class }}(CMSPlugin):
    title = models.CharField(_('title'), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
