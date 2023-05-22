from django.db import models

class Categories(models.Model):
    STATUS = [
        ("new", "Новая"),
        ("old", "Старая")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS, default="new", max_length=10)

    def __str__(self):
        return self.name