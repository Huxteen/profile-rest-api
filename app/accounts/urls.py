from django.contrib import admin
from django.urls import path, include
from accounts import views

# We use this when we use a viewset
from rest_framework.routers import DefaultRouter

#For ModelViewSet you dont need to register with a base name
# Django URLS would automatically figure this out. 
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('profile-home', views.profile, name='profile'),
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),

]
   