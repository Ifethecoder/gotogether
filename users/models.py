from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=200, null=False)
    going_to = models.CharField(max_length=200, null=False)
    by_this_date_and_time = models.DateTimeField(null=False)
    minerva_email = models.EmailField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.current_location + "\n" + self.going_to