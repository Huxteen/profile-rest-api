from django.contrib import admin
from django.urls import path, include
from accounts import views

# We use this when we use a viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('profile-home', views.profile, name='profile'),
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),

]
   