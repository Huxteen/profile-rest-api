from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


from accounts import serializers
from accounts import permissions
from accounts import models

# Create your views here.

class HelloApiView(APIView):
    """ Test API View. """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of APIView features. """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete).'
            'Its is similar to a traditional django view',
            'Gives you the most control over your login',
            'Is mapped manually to URLS'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self, request):
        """ Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

    
    def patch(self, request, pk=None):
        """Patch request only update fields provided in the request."""


        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Delete an object. """

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Returns a Hello Message."""
    
        a_viewset = [
            'Uses actions( list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello ViewSet', 'a_viewset':a_viewset})

    def create(self, request):
        """ Create a new Hello message."""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID."""
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """ Handle updating an object by its ID."""
        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """ Handle partial update an object by its ID."""
        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """ Handle dELETE an object by its ID."""

        return Response({'http_method': 'DELETE'})
          
    
def profile(request):
    pass


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer
    
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Set the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)

