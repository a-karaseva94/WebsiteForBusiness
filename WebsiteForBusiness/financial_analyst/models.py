from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    """
        Модель Услуги:
        TYPES_CHOICES - список видов услуг для выбора
        PROGRAMS_CHOICES - список программ услуг для выбора
        title - имя услуги (с ограничением длины)
        type - вид услуги (с выбором из списка TYPES_CHOICES)
        program - программа услуги (с выбором из списка PROGRAMS_CHOICES)
        cost - цена услуги (с ограничением длины и знаков после запятой)
        Модель содержит метод и класс
    """
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
    type = models.CharField(max_length=100,choices=TYPES_CHOICES, verbose_name='Вид займа')
    program = models.CharField(max_length=100,choices=PROGRAMS_CHOICES, verbose_name='Программа займа')
    cost = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='Цена услуги')

    def __str__(self):
        """
            Вывод в консоль
        """
        return self.title

    class Meta:
        """
            Класс Meta - внутренний класс:
            verbose_name - настройка имени поля в админ-панели
            verbose_name_plural - настройка названия модели в админ-панели
        """
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class CartItem(models.Model):
    """
        Модель Корзины:
        service - связь с моделью Услуги
        quantity - количество услуг в корзине
        user - связь с моделью User (модель по умолчанию)
        date_added - дата добавления в корзину (автоматически)
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
            Вывод в консоль
        """
        return f'{self.quantity} x {self.service}'
