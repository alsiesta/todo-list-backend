from django.db import models
from django.utils import timezone
from django.conf import settings

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(default=timezone.now)
    checked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
                                      
                                      
