# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Comercio, Tag, Cidade, Evento, Post, Promocao
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q

# Create your views here.
# pagina index
def index(request):

    # lista com todas as cidades
    cidades = Cidade.objects.list_cidade()

    # lista com os eventos mais proximos
    eventos = Evento.objects.list_quant(6)

    context = {"title": "SeridoTem", 'cidades': cidades, 'eventos': eventos}
    return render(request, 'divulgacoes/index.html', context)

# pagina sobre
def sobre(request):

    # passa o titulo
    context = {"title": "Sobre"}
    return render(request, 'divulgacoes/sobre.html', context)

# pagina lista de festas
def eventos(request):

    # retorna a lista de todos os eventos válidos (que ainda não aconteceram)
    eventos = Evento.objects.list_eventos()

    # paginacao
    paginator = Paginator(eventos, 16) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        evento = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        evento = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        evento = paginator.page(paginator.num_pages)

    context = {"title": "Eventos", 'eventos': evento}
    return render(request, 'divulgacoes/eventos.html', context)

# detalhe do evento
def detalhe_evento(request, pk):

    # pega o evento
    evento = get_object_or_404(Evento, pk=pk)

    context = {"title": evento.titulo, 'evento': evento}

    return render(request, 'divulgacoes/detalhe_evento.html', context)

# paginas de noticias
def noticias(request):

    # query de noticias
    noticias = Post.objects.list_post()

    # paginacao
    paginator = Paginator(noticias, 10) # Show 15 contacts per page

    # requesita a página
    page = request.GET.get('page')
    try:
        noticia = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        noticia = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        noticia = paginator.page(paginator.num_pages)

    context = {"title": "Notícias", 'noticias': noticia}
    return render(request, 'divulgacoes/noticias.html', context)

# detalhe noticia
def detalhe_noticia(request, pk):

    # pega o id da noticia
    noticia = get_object_or_404(Post, pk=pk)

    # passa os valores apra a context
    context = {"title": noticia.titulo, 'noticia': noticia}
    
    return render(request, 'divulgacoes/detalhe_noticia.html', context)

# lista de acordo com as informçãoes inseridas na (index)
def pesquisa_index(request):

    # dados que vem do formulário de pesquisa
    cidade = request.GET.get("cidade")
    tag = request.GET.get("tag")

    # pego todas as tag para exibir na página
    tags = Tag.objects.list_tags()
    
    # query contendo as promocoes da cidade listada
    promocoes = Promocao.objects.list_promocao_cidade(cidade)

    # query para mostrar o nome da cidade na página
    nome_cidade = Cidade.objects.filter(Q(id=cidade))

    # passa o ID da cidade (mesma variavel para todas as funções)
    id_cidade = cidade

    # query que traz as empresas do tipo e da cidade selecionada
    comercios = Comercio.objects.list_comercios_tags(cidade, tag)

    # paginacao
    paginator = Paginator(comercios, 18) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        comercio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comercio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comercio = paginator.page(paginator.num_pages)

    context = {"title": "Pesquisa", "comercios": comercio, "tags": tags, 'promocoes': promocoes, 'nome_cidade': nome_cidade, 'id_cidade': id_cidade, 'cidade': cidade, 'tag': tag}
    return render(request, 'divulgacoes/pesquisa_comercio.html', context)

# query relacioanda a pesquisa de tipo dentro da cidade selecionada (pesquisa_cidade)
def pesquisa_comercio(request):

    # pega os valores vindos do formuláro
    nome = request.GET.get("nome")
    tag = request.GET.get("tag")
    cidade = request.GET.get("cidade")

    # lista com todas as tags
    tags = Tag.objects.list_tags()

    # query contendo as promocoes da cidade listada
    promocoes = Promocao.objects.list_promocao_cidade(cidade)

    # query para mostrar o nome da cidade na página    
    nome_cidade = Cidade.objects.filter(Q(id=cidade))

    # passa o ID da cidade (mesma variavel para todas as funções)
    id_cidade = cidade

    # query com os comercios resultante das buscas (nome ou tipo do campo nome e tipo do campo tip)
    comercios = Comercio.objects.list_pesquisa_comercio(nome, tag, cidade)

    # paginacao
    paginator = Paginator(comercios, 18) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        comercio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comercio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comercio = paginator.page(paginator.num_pages)

    # passo os valores (cidade, nome e tag para poder usar na paginação)    
    context = {"title": "Pesquisa", "comercios": comercio, "tags": tags, 'promocoes': promocoes, 'nome_cidade': nome_cidade, 'id_cidade': id_cidade, 'cidade': cidade, 'nome': nome, 'tag': tag}
    return render(request, 'divulgacoes/pesquisa_comercio.html', context)

# lista todos os comercios da cidade selecionada (index)
def pesquisa_cidade(request, cidade):
    # envio o valor de cidade para a pagina

    # lista com todos os tempos
    tags= Tag.objects.list_tags()

    # lista das promocoes da cidade
    promocoes = Promocao.objects.list_promocao_cidade(cidade)

    # passo a cidade que esta selecionada
    nome_cidade = Cidade.objects.filter(Q(id=cidade))

    # passo o ID em um valor unico, para ser usado na busca
    id_cidade = cidade

    # query que tras todos os comercios da cidade selecioanda
    comercios = Comercio.objects.list_comercios_cidade(cidade)

    # paginacao
    paginator = Paginator(comercios, 18) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        comercio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comercio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comercio = paginator.page(paginator.num_pages)

    context = {"title": "Busca cidade", 'tags': tags, 'promocoes': promocoes, 'comercios': comercio, 'nome_cidade': nome_cidade, 'id_cidade': id_cidade, 'cidade': cidade}
    return render(request, 'divulgacoes/pesquisa_comercio.html', context)

# query da lista de atalho (pesquisa_comercio)
def pesquisa_atalho(request, cidade, tag):

    # lista com todos os tempos
    tags= Tag.objects.list_tags()

    # lista das promocoes da cidade
    promocoes = Promocao.objects.list_promocao_cidade(cidade)

    # passo a cidade que esta selecionada
    nome_cidade = Cidade.objects.filter(Q(id=cidade))

    # passo o ID em um valor unico, para ser usado na busca
    id_cidade = cidade

    # query que tras todos os comercios da cidade selecioanda
    comercios = Comercio.objects.list_comercios_tags(cidade, tag)

    # paginacao
    paginator = Paginator(comercios, 18) # Show 25 contacts per pag
    page = request.GET.get('page')
    try:
        comercio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comercio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comercio = paginator.page(paginator.num_pages)

    context = {"title": "Busca cidade", 'tags': tags, 'promocoes': promocoes, 'comercios': comercio, 'nome_cidade': nome_cidade, 'id_cidade': id_cidade, 'cidade': cidade, 'tag': tag}
    return render(request, 'divulgacoes/pesquisa_comercio.html', context)

# detalhes do comercio
def detalhe_comercio(request, pk):
    comercio = get_object_or_404(Comercio, pk=pk)
    context = {"title": comercio.nome, 'comercio': comercio}
    return render(request, 'divulgacoes/detalhe_comercio.html', context)
