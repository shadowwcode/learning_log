# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from learning_logs import models

admin.site.register(models.Topic)

admin.site.register(models.Entry)