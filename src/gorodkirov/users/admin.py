from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user']
    raw_id_fields = ['user']
    search_fields = ['user__username', 'user__first_name',
                     'user__last_name', 'user__email']


admin.site.register(Profile, ProfileAdmin)
