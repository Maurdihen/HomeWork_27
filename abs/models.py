from django.db import models

class Abs(models.Model):
    STATUS = [
        ("draft", "Черновик"),
        ("open", "Открыта"),
        ("closes", "Закрыта")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=150)
    status = models.CharField(choices=STATUS, default="draft", max_length=10)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return "abs"
