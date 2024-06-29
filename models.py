from django.db import models

class Book(models.Model):
    title = models.Charfiel(max_length=155, unique=True, null=False)
    description = models.TextField()
    author = models.CharFiel(max_length=255)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def get_queryset(self):
        return self.objects.all


    def  __str__(self):
        return self.title

