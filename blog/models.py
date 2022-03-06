from django.db import models
from utils.models import BaseAbstractModel
from authentication.models import User

# Create your models here.
class Post(BaseAbstractModel):
    """model for a post"""

    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
