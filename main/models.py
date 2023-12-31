from django.db import models

# Create your models here.
from django.db import models

class ImagePair(models.Model):
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.title

class Devi(models.Model):
    TYPE_CHOICES = (
        ('society', 'Société'),
        ('particular', 'Particulier'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    prestation_id = models.IntegerField()
    observation = models.TextField()

    def __str__(self):
        return self.name

class AvisUtilisateur(models.Model):
    commentaire = models.TextField()
    def __str__(self):
        return f"Avis {self.id}"

class Video(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email