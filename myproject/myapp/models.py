from django.db import models

# Create your models here.


class Todo(models.Model):
    created_by = models.CharField(max_length=20)
    created_on = models.DateTimeField()
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title
