from django.db import models
from projects.models import Projects


class Contacts(models.Model):
    '''
    Модель контактов
    '''
    name = models.CharField(verbose_name='Имя', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=100)
    organization = models.CharField(verbose_name='Название организации', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Payment(models.Model):
    '''
    Модель типа оплаты
    '''

    name = models.CharField(verbose_name='Тип оплаты', max_length=100, help_text='Наличный, безналичный')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'


class Status(models.Model):
    name = models.CharField(verbose_name='Статус', max_length=100, help_text='Активен, архивен')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Clients(models.Model):
    '''
    Модель клиента
    '''

    project = models.ForeignKey(Projects, verbose_name='Проект', on_delete=models.CASCADE)
    contacts = models.ForeignKey(Contacts, verbose_name='Контакт', on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, verbose_name='Тип оплаты', on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE)

    def __str__(self):
        return self.project

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'