from django.db import models

class Post(models.Model):
    baslik = models.CharField(max_length=120)
    icerik = models.TextField()
    olusturma_tarih = models.DateTimeField()

