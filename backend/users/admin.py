from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



# Register your models here.
from users.models import User, FavoriteMotion

class UserAdmin(UserAdmin):
    list_display = [
        'username',
        'email',
    ]

class FavoriteAdmin(admin.ModelAdmin):
    model = FavoriteMotion
    list_display = [
        'id',
        'user',
        'motion'
    ]

admin.site.register(User, UserAdmin)
admin.site.register(FavoriteMotion, FavoriteAdmin)
