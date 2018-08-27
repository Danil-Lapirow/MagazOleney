from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    owner = models.ForeignKey(User, models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_at = models.DateField(auto_created=True)
    published_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
