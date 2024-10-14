# webtoons/urls.py
from django.urls import path
from .views import WebtoonListCreate, WebtoonDetail

urlpatterns = [
    path('webtoons/', WebtoonListCreate.as_view(), name='webtoon-list-create'),
    path('webtoons/<int:pk>/', WebtoonDetail.as_view(), name='webtoon-detail'),
]
