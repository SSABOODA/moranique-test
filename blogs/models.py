from django.db import models

from accounts.models import User


class Blog(models.Model):
    user       = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title      = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    body       = models.TextField()

    class Meta:
        db_table = 'blogs'
