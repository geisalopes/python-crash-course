from django.contrib import admin  # type: ignore

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

# Register your models here.
