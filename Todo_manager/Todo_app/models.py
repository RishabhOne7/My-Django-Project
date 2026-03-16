from django.db import models

# Create your models here.

class tasks (models.Model):
    Task_Name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Task_Name} {self.status}"