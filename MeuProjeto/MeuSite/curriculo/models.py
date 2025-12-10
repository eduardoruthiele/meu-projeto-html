from django.db import models

class ItemRanking(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class LinkItem(models.Model):
    nome = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    item = models.ForeignKey(ItemRanking, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
