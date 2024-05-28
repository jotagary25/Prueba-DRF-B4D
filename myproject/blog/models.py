from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# for post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    state = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title