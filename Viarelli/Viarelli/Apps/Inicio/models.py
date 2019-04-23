from django.db import models

# Create your models here.

class Presentacion(models.Model):
    title = models.CharField(max_length=45)
    info = models.ImageField(upload_to='post_image')
    image = models.ImageField(upload_to='post_image')

class mision(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()

class vision2(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()

class balance(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='post_image', null=True)

class date(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='post_image')
    nota = models.CharField(max_length=150)
    title2 = models.CharField(max_length=20)
    image2 = models.ImageField(upload_to='post_image')

class verfication(models.Model):
    title1 = models.CharField(max_length=20)
    image1 = models.ImageField(upload_to='post_image')
    image11 = models.ImageField(upload_to='post_image')
    title2 = models.CharField(max_length=20)
    image2 = models.ImageField(upload_to='post_image')
    image22 = models.ImageField(upload_to='post_image')
    title3 = models.CharField(max_length=20)
    image3 = models.ImageField(upload_to='post_image')
    image33 = models.ImageField(upload_to='post_image')
    title4 = models.CharField(max_length=20)
    image4 = models.ImageField(upload_to='post_image')
    image44 = models.ImageField(upload_to='post_image')
    objetivos = models.ImageField(upload_to='post_image')

class planilla(models.Model):
    title = models.CharField(max_length=20)
    image1 = models.ImageField(upload_to='post_image')
    image2 = models.ImageField(upload_to='post_image')
    image3 = models.ImageField(upload_to='post_image')

class canvas(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='post_image')

