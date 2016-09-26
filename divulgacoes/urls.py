from django.conf.urls import include, url
from . import views

app_name = 'divulgacoes'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^sobre/$', views.sobre, name="sobre"),
    url(r'^eventos/$', views.eventos, name="eventos"),
    url(r'^noticias/$', views.noticias, name="noticias"),
    url(r'^(?P<pk>.+)/detalhe_noticia/$', views.detalhe_noticia, name="detalhe_noticia"),
    url(r'^(?P<pk>.+)/detalhe_evento/$', views.detalhe_evento, name="detalhe_evento"),
    url(r'^pesquisa_form/$', views.pesquisa_form, name="pesquisa_form"),
    url(r'^(?P<cidade>[0-9]+)/pesquisa_cidade/$', views.pesquisa_cidade, name="pesquisa_cidade"),
    url(r'^(?P<cidade>[0-9]+)/(?P<tag>\w+)/pesquisa_tipo/$', views.pesquisa_tipo, name="pesquisa_tipo"),
    url(r'^(?P<pk>[0-9]+)/detalhe_comercio/$', views.detalhe_comercio, name="detalhe_comercio"),
]