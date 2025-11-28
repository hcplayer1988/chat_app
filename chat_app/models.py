from django.db import models

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True )
    
    def __str__(self):
        return f"{self.name}: {self.message}"