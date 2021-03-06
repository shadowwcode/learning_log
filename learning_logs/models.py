# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    ''' 用户学习的主题 '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):
    '''学到的有关主题的具体信息'''
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text