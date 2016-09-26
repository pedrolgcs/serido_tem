from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Comercio, Tag, Cidade, Evento, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q


# Create your views here.
# pagina index
def index(request):
    # lista com todas as cidades
    cidades = Cidade.objects.all().order_by('nome')
    # lista com os eventos mais proximos
    eventos = Evento.objects.order_by('data').filter(Q(data__gte=timezone.now()))[:4]

    context = {"title": "SeridoTem", 'cidades': cidades, 'eventos': eventos}
    return render(request, 'divulgacoes/index.html', context)

 # pagina sobre

 # pagina sobre
def sobre(request):
    context = {"title": "Sobre"}
    return render(request, 'divulgacoes/sobre.html', context)

# pagina lista de festas
def eventos(request):
    eventos = Evento.objects.order_by('data').filter(Q(data__gte=timezone.now()))

    # paginacao
    paginator = Paginator(eventos, 15) # Show 25 contacts per page
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
    evento = get_object_or_404(Evento, pk=pk)
    context = {"title": evento.title, 'evento': evento}
    return render(request, 'divulgacoes/detalhe_evento.html', context)

# paginas de noticias
def noticias(request):
    noticias = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    # paginacao
    paginator = Paginator(noticias, 15) # Show 15 contacts per page
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

def detalhe_noticia(request, pk):
    noticia = get_object_or_404(Post, pk=pk)
    context = {"title": noticia.title, 'noticia': noticia}
    return render(request, 'divulgacoes/detalhe_noticia.html', context)

# lista todos os comercios da cidade selecionada
def pesquisa_cidade(request, cidade):
    # passo a cidade que esta selecionada
    nome_cidade = Cidade.objects.filter(Q(id=cidade))
    # passo o ID em um valor unico, para ser usado na busca
    id_cidade = cidade
    # lista com todos os tempos
    tags= Tag.objects.all()
    # query contendo os comercios da cidade selecionada
    comercios = Comercio.objects.all().filter(Q(cidade_id=cidade)).order_by('nome')

    # paginacao
    paginator = Paginator(comercios, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        comercio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comercio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comercio = paginator.page(paginator.num_pages)

    context = {"title": "Busca cidade", 'tags': tags, 'comercios': comercio, 'nome_cidade': nome_cidade, 'id_cidade': id_cidade}
    return render(request, 'divulgacoes/pesquisa_comercio.html', context)

# lista os comercios com o referente tipo na cidade selecionada
def pesquisa_tipo(request, tag, cidade):
    tags = Tag.objects.all()
    nome_cidade = Cidade.objects.filter(Q(id=cidade))
    id_cidade = cidade
    comercios = Comercio.objects.all().filter(Q(cidade_id=cidade) & (Q(tags__icontains=tag))).order_by('nome')

    # paginacao
    paginator = Paginator(comercios, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        comercio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comercio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comercio = paginator.page(paginator.num_pages)

    context = {"title": "Pesquisa", "comercios": comercio, "tags": tags, 'nome_cidade': nome_cidade, 'id_cidade': id_cidade}
    return render(request, 'divulgacoes/pesquisa_comercio.html', context)

# lista de acordo com as informçãoes inseridas na tela inicial
def pesquisa_form(request):

    tags = Tag.objects.all()

    # dados que vem do formulário do index
    cidade = request.GET.get("cidade")
    tag = request.GET.get("tag")

    nome_cidade = Cidade.objects.filter(Q(id=cidade))
    id_cidade = cidade

    comercios = Comercio.objects.all().filter((Q(nome__icontains=tag) | (Q(tags__icontains=tag))) & (Q(cidade_id=cidade))).order_by('nome')

    # paginacao
    paginator = Paginator(comercios, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        comercio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comercio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comercio = paginator.page(paginator.num_pages)

    context = {"title": "Pesquisa", "comercios": comercio, "tags": tags, 'nome_cidade': nome_cidade, 'id_cidade': id_cidade}
    return render(request, 'divulgacoes/pesquisa_comercio.html', context)

# detalhes do comercio
def detalhe_comercio(request, pk):
    comercio = get_object_or_404(Comercio, pk=pk)
    context = {"title": comercio.nome, 'comercio': comercio}
    return render(request, 'divulgacoes/detalhe_comercio.html', context)