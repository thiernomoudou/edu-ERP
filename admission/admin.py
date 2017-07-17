from django.contrib import admin

# Register your models here.
from  .models import Saisie
from  .models import Inscription

admin.site.register(Saisie)
admin.site.register(Inscription)