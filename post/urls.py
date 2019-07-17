from django.urls import path, include
from rest_framework.routers import DefaultRouter ## RESTful에서 사용할 Router 개념
from . import views 

router = DefaultRouter() ## Not Yet
router.register('post', views.PostViewSet) ## Not Yet

urlpatterns = [
    path('', include(router.urls)),
]
