from django.db import models
from projects.models import Projects


class Positions(models.Model):
    name = models.CharField(verbose_name='Должность', max_length=100, help_text='Программист, копирайтер, дизайнер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class PaymentType(models.Model):
    name = models.CharField(verbose_name='Тип оплаты', max_length=100, help_text='Оклад, почасовая оплата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'


class Creators(models.Model):
    '''
    Модель исполнителя
    '''

    project = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.CASCADE)
    name = models.TextField(verbose_name='Имя', max_length=1000)
    post = models.ForeignKey(Positions, verbose_name='Должность', on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, verbose_name='Тип оплаты', on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='Сумма', max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
