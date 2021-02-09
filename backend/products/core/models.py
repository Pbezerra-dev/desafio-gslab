from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=55)
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(
        verbose_name='Preço',
        max_digits=15,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(1)],
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return self.name
