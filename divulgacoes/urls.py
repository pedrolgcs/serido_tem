from django.conf.urls import include, url
from . import views

app_name = 'divulgacoes'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^sobre$', views.sobre, name="sobre"),
    url(r'^eventos/$', views.eventos, name="eventos"),
    url(r'^detalhe_evento/(?P<pk>.+)$', views.detalhe_evento, name="detalhe_evento"),
    url(r'^noticias/$', views.noticias, name="noticias"),
    url(r'^detalhe_noticia/(?P<pk>.+)$', views.detalhe_noticia, name="detalhe_noticia"),
    url(r'^pesquisa/$', views.pesquisa_index, name="pesquisa_index"),
    url(r'^comercios/$', views.pesquisa_comercio, name="pesquisa_comercio"),
    url(r'^pesquisa/(?P<cidade>[0-9]+)$', views.pesquisa_cidade, name="pesquisa_cidade"),
    url(r'^pesquisa/(?P<cidade>[0-9]+)/(?P<tag>\w+)/$', views.pesquisa_atalho, name="pesquisa_atalho"),
    url(r'^pesquisa/(?P<cidade>[0-9]+)$', views.pesquisa_cidade, name="pesquisa_cidade"),
    url(r'^detalhe_comercio/(?P<pk>[0-9]+)$', views.detalhe_comercio, name="detalhe_comercio"),
]