#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Todo(models.Model):
    """
    """
    PRIORITY = ((1, '优先级1'), (2, '优先级2'), (3, '优先级3'), (4, '优先级4'))

    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField(blank=True, default='')
    # 时间： 创建/修改/截止
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    expire_time = models.DateTimeField(null=True, blank=True)
    # 优先级
    priority = models.IntegerField(choices=PRIORITY, null=True, blank=True)
    # 完成标记
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, related_name='todos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'todoist'
        ordering = ("-created_time", )  # 按创建时间逆序显示

    def __str__(self):
        return "Todo: {} created_time: {} expire_time: {} completed: ".format(
            self.title, self.created_time, self.expire_time, self.completed)
