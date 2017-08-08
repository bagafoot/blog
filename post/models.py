from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name="title")
    content = models.TextField(verbose_name="content")
    publishing_dttm = models.DateTimeField(verbose_name="publishing date", default=datetime.now())

    def __str__(self):
        return "{title},{publising}".format(title=self.title,publising=self.publishing_dttm)

