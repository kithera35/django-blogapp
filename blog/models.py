from ast import Delete
from email.policy import default
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    




