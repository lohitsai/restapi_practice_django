from django.shortcuts import render, HttpResponse
from django.http import Http404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
