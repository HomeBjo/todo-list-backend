from django.conf import settings
from django.db import models
from datetime import date

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    my_field = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f'({self.id}) {self.title}'