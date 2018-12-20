#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from todoist.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('id', 'owner', 'title', 'body', 'priority', 'mark',
                  'expire_time', 'created_time', 'modified_time')
        read_only_fields = ('owner', 'create_time')


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'todos')
