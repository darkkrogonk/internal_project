from django.db import models


class TypeProjects(models.Model):
    '''
    Модель типа проекта
    '''

    name = models.CharField(verbose_name='Тип', max_length=100, help_text='Сайт, телеграмм бот, реклама, другое')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип проекта'
        verbose_name_plural = 'Типы проекта'


class Projects(models.Model):
    '''
    Модель проекта
    '''

    title = models.TextField(verbose_name='Название', max_length=1000)
    type_project = models.ForeignKey(TypeProjects, verbose_name='Тип проекта', on_delete=models.SET_NULL, null=True)
    amount_client = models.DecimalField(verbose_name='Сумма для клиента', max_digits=11, decimal_places=2, default=0)
    amount_planned_cost = models.DecimalField(verbose_name='Сумма планируемых затрат', max_digits=11, decimal_places=2, default=0)
    amount_actual_costs = models.DecimalField(verbose_name='Сумма фактических затрат', max_digits=11, decimal_places=2, default=0)
    date_start = models.DateField(auto_now_add=True)
    date_planned_completion = models.DateField(auto_now_add=True)
    date_actual_completion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
