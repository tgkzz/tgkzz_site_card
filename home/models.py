from django.db import models
from django.urls import reverse


class Skills(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_post', kwargs={'post_id': self.pk})
