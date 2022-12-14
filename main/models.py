from django.db import models


class Hall(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Вместимость')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return 'Зал - ' + str(self.name)

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото блюда')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return 'Блюдо - ' + str(self.name)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Order(models.Model):

    TIME_OF_DAY_CHOICES = (
        ('morning', 'Утро'),
        ('day', 'День'),
        ('evening', 'Вечер'),
    )

    fullname = models.CharField(max_length=150, verbose_name='ФИО')
    date = models.DateTimeField(verbose_name='Дата торжества')
    time_of_day = models.CharField(choices=TIME_OF_DAY_CHOICES, verbose_name='Время дня', max_length=30)
    dishes = models.ManyToManyField(Dish, verbose_name='Блюда')
    number_of_people = models.IntegerField(verbose_name='Кол-во людей')
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Зал')
    agree = models.BooleanField(verbose_name='Согласие на обработку персональных данных')

    def __str__(self):
        return f'Заказ {str(self.id)} на {self.fullname}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


