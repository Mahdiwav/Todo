from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model

user = get_user_model()


# Create your models here.
class Todo(models.Model):
    titel = models.CharField(max_length=50)
    text = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')

    class Meta:
        db_table = 'todos'