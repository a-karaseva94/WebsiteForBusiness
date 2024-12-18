from django.db import models
from django.contrib.auth.models import User


# class Buyer(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     created_at = models.DateTimeField(auto_now=True)
#
#
#     def __str__(self):
#         return self.name
#
#
#     class Meta:
#         verbose_name = 'Покупатель'
#         verbose_name_plural = 'Покупатели'
#         ordering = ['-created_at']


class Service(models.Model):
    TYPES_CHOICES = [
        ('для регионального займа', 'для регионального займа'),
        ('для совместного займа', 'для совместного займа'),
    ]
    PROGRAMS_CHOICES = [
        ('Проекты развития с регфондами', 'Проекты развития с регфондами'),
        ('Комплектующие изделия с регфондами', 'Комплектующие изделия с регфондами'),
        ('Производительность труда с регфондами', 'Производительность труда с регфондами'),
        ('Проекты лесной промышленности с регфондами', 'Проекты лесной промышленности с регфондами'),
        ('Региональные проекты развития', 'Региональные проекты развития'),
    ]
    title = models.CharField(max_length=50, verbose_name='Услуга')
    type = models.CharField(max_length=70, choices=TYPES_CHOICES, verbose_name='Вид займа')
    program = models.CharField(max_length=70, choices=PROGRAMS_CHOICES, verbose_name='Программа займа')
    cost = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Цена услуги')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class CartItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.service}'