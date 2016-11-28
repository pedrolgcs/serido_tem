from django.db import models
from django.db.models import Q
from django.utils import timezone
# Create your models here.

# -*- coding: utf-8 -*-
def upload_location_cidade(instance, filename):
    return "Cidade/%s/%s" % (instance.nome, filename)

def upload_location_tag(instance, filename):
    return "tipo/%s/%s" % (instance.nome, filename)

def upload_location(instance, filename):
    return "comercio/%s/%s" % (instance.nome, filename)

def upload_location_evento(instance, filename):
    return "evento/%s/%s" % (instance.title, filename)

def upload_location_post(instance, filename):
    return "post/%s/%s" % (instance.title, filename)

def upload_location_promocao(instance, filename):
    return "promocao/%s/%s" % (instance.title, filename)

# Create your models here.

# CIDADE
class CidadeManager(models.Manager):

    # retorna todas as cidades cadastradas
    def list_cidade(self):
         return Cidade.objects.all().order_by('nome')

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to=upload_location_cidade, null=True, blank=True)
    objects = CidadeManager()
    
    def __str__(self):
        # return self.nome + "," + self.descricao[:20] + "..."
        return self.nome


# TAGS
class TagManager(models.Manager):
    # lista todas as tags
    def list_tags(self):
         return Tag.objects.all().order_by('nome')

class Tag(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    icone = models.ImageField(upload_to=upload_location_tag, null=True, blank=True)
    objects = TagManager()

    def __str__(self):
        return self.nome


# COMERCIOS
class ComercioManager(models.Manager):
    # query que traz as empresas do tipo e da cidade selecionada
    def list_comercios_tags(self, cidade, tag):
        return Comercio.objects.all().filter((Q(nome__icontains=tag) | (Q(tags__icontains=tag))) & (Q(cidade_id=cidade))).order_by('nome')

    def list_pesquisa_comercio(self, nome, tag, cidade):
        return Comercio.objects.all().filter(Q(cidade_id=cidade) & (Q(tags__icontains=nome)) & (Q(tags__icontains=tag))).order_by('nome')
        
    def list_comercios_cidade(self, cidade):
        return Comercio.objects.all().filter(Q(cidade_id=cidade)).order_by('nome')

class Comercio(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=upload_location,null=True, blank=True)
    descricao = models.TextField()
    tags = models.CharField(max_length=400)
    faz_entrega = models.CharField(max_length=50, null=True, blank=True)
    cartao = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    telefone2 = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=150, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    referencia = models.CharField(max_length=200, null=True, blank=True)
    mapa = models.CharField(max_length=500, null=True, blank=True)
    funcionamento = models.CharField(max_length=350)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    twitter = models.CharField(max_length=300, null=True, blank=True)
    instagram = models.CharField(max_length=300, null=True, blank=True)
    banner1 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner2 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner3 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner4 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner5 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner6 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    objects = ComercioManager()

    def __str__(self):
        return self.nome


# EVENTOS
class EventoManager(models.Manager):

    # retorna uma quantidade x de eventos
    def list_quant(self,quant):
         return Evento.objects.order_by('data').filter(Q(data__gte=timezone.now()))[:quant]

    # retorna a lista de todos os eventos válidos (que ainda nao aconteceram)
    def list_eventos(self):
        return Evento.objects.order_by('data').filter(Q(data__gte=timezone.now()))

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=400)
    preco = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to=upload_location_evento,null=True, blank=True)
    banner = models.ImageField(upload_to=upload_location_evento,null=True, blank=True)
    objects = EventoManager()

    def __str__(self):
        return self.titulo


# POST
class PostManager(models.Manager):

    # retorna todas as postagens
    def list_post(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=200)
    texto = models.TextField()
    thumbnail = models.ImageField(upload_to=upload_location_post,null=True, blank=True)
    video = models.CharField(max_length=1000, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    objects = PostManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


# PROMOCAO
class PromocaoManager(models.Manager):
    def list_promocao_cidade(self, cidade):
         return Promocao.objects.filter(Q(published_date__lte=timezone.now()) & (Q(validade__gte=timezone.now()) & (Q(cidade=cidade))))

class Promocao(models.Model):
    comercio = models.ForeignKey(Comercio, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    validade = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    banner = models.ImageField(upload_to=upload_location_promocao,null=True, blank=True)
    objects = PromocaoManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo