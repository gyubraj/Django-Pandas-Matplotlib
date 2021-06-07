from django.contrib import admin
from .models import Position,CSV,Sale
# Register your models here.
admin.site.register([Position,CSV,Sale])