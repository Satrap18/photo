from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.email