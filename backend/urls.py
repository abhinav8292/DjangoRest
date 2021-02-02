from django.db import router
from rest_framework import routers, urlpatterns
from django.urls import path
from django.conf.urls import url, include

from .views import*
from . import views

router = routers.DefaultRouter()
router.register('posts', PostViewSet, 'posts')


#urlpatterns =  router.urls
urlpatterns = [
    url(r'^$', views.APIRoot.as_view()),
    url(r'', include(router.urls)),
]
