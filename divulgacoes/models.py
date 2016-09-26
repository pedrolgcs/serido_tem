from django.db import models
# Create your models here.

def upload_location_cidade(instance, filename):
    return "cidade/%s/%s" % (instance.nome, filename)

def upload_location_tag(instance, filename):
    return "tipo/%s/%s" % (instance.nome, filename)

def upload_location(instance, filename):
    return "comercio/%s/%s" % (instance.nome, filename)

def upload_location_evento(instance, filename):
    return "evento/%s/%s" % (instance.title, filename)

def upload_location_post(instance, filename):
    return "post/%s/%s" % (instance.title, filename)


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to=upload_location_cidade, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.ImageField(upload_to=upload_location_tag, null=True, blank=True)

    def __str__(self):
        return self.nome

class Comercio(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=upload_location,null=True, blank=True)
    descricao = models.TextField()
    tags = models.CharField(max_length=400)
    faz_entrega = models.CharField(max_length=50, null=True)
    cartao = models.CharField(max_length=60, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True)
    telefone = models.CharField(max_length=20, null=True)
    bairro = models.CharField(max_length=100, null=True)
    rua = models.CharField(max_length=150, null=True)
    numero = models.CharField(max_length=20, null=True)
    referencia = models.CharField(max_length=200, null=True)
    funcionamento = models.CharField(max_length=350)
    facebook = models.CharField(max_length=300, null=True)
    banner1 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner2 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner3 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner4 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner5 = models.ImageField(upload_to=upload_location,null=True, blank=True)
    banner6 = models.ImageField(upload_to=upload_location,null=True, blank=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=400)
    preco = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to=upload_location_evento,null=True, blank=True)
    banner = models.ImageField(upload_to=upload_location_evento,null=True, blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = models.ImageField(upload_to=upload_location_post,null=True, blank=True)
    video = models.CharField(max_length=1000)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

