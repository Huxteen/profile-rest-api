from django.contrib import admin
from accounts.models import UserProfile, ProfileFeedItem

admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)