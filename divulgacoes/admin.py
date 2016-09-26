from django.contrib import admin

from .models import Tag, Comercio, Evento, Cidade, Post
# Register your models here.

admin.site.register(Cidade)
admin.site.register(Tag)
admin.site.register(Comercio)
admin.site.register(Evento)
admin.site.register(Post)
