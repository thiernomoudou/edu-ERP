from django.contrib import admin

# Register your models here.
from .models import User, Role, UserHasRole

admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserHasRole)

