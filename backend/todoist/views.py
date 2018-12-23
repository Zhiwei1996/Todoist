#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.shortcuts import render

from todoist.models import Todo
from todoist.serializers import TodoSerializer
from todoist.serializers import UserSerializer
from todoist.permissions import IsOwnerOrReadOnly

from rest_framework import mixins, generics, permissions

# Create your views here.


def index(request):
    return render(request, 'todoist/index.html', context={
        'title': 'Hello',
        'welcome': 'Hello, World'
    })


class TodoList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
