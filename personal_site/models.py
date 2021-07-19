from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title