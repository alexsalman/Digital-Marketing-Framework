from django.contrib import admin
from .models import UserProfile, UploadVideo

class UserProfile_Admin(admin.ModelAdmin):
    list_display = ('user', 'address_country')
    search_fields = ('user',)

class UploadVideo_Admin(admin.ModelAdmin):
    list_display = ('user', 'description', 'uploaded_at')
    search_fields = ('user',)

admin.site.register(UserProfile, UserProfile_Admin)
admin.site.register(UploadVideo, UploadVideo_Admin)
