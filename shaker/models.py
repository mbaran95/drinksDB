from django.db import models


alcoholType = (
    (1, 'Vodka'),
    (2, 'Whisky'),
    (3, 'Gin'),
    (4, 'Tequila'),
    (5, 'Rum'),
    (6, 'Rakija'),
)


class Drinks(models.Model):
    name_drink = models.CharField(max_length=100)
    desc_drink = models.CharField(max_length=100)
    alcohol_type = models.IntegerField(choices=alcoholType)

    def __str__(self):
        return self.name_drink


class Ingredients(models.Model):
    drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE)
    name_ingredient = models.CharField(max_length=100)

    def __str__(self):
        return self.name_ingredient
