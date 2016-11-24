from django.contrib import admin

from .models import Tag, Comercio, Evento, Cidade, Post, Promocao
# Register your models here.

admin.site.register(Cidade)
admin.site.register(Tag)
admin.site.register(Comercio)
admin.site.register(Evento)
admin.site.register(Post)
admin.site.register(Promocao)
