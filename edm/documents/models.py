import datetime
import os

from django.db import models
from config.settings import MEDIA_ROOT


def DocTemplateUploadPath(instance, filename):
    """Путь загрузки шаблона документа"""
    path = f'{MEDIA_ROOT}\\templates\\{instance.category.type.kind.kind}\\{instance.category.type.type}\\'
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    path += f'{instance.category.category}.docx'
    return path


class DocKinds(models.Model):
    """Модель видов документов"""
    kind = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Виды документов'
    )

    objects = models.Manager()

    def __str__(self):
        return self.kind

    def delete(self, using=None, keep_parents=False):
        if self.id != 1:
            super(DocKinds, self).delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = 'Вид документа'
        verbose_name_plural = 'Виды документов'


class DocTypes(models.Model):
    """Модель типов документов"""
    kind = models.ForeignKey(
        DocKinds,
        on_delete=models.CASCADE,
        default=1,
        null=True,
        verbose_name='Вид документа'
    )
    type = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Тип документа'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.kind.kind} - {self.type}'

    def delete(self, using=None, keep_parents=False):
        if self.id != 1:
            super(DocTypes, self).delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'
        unique_together = ('kind_id', 'type')


class DocTypeCategories(models.Model):
    """Модель категорий типа документа"""
    type = models.ForeignKey(
        DocTypes,
        on_delete=models.CASCADE,
        default=1,
        null=True,
        verbose_name='Тип документа'
    )
    category = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Категория документа'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.type.type} - {self.category}'

    def delete(self, using=None, keep_parents=False):
        if self.id != 1:
            super(DocTypeCategories, self).delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = 'Категория типа документа'
        verbose_name_plural = 'Категории типов документов'
        unique_together = ('type_id', 'category')


class DocRequisiteTypes(models.Model):
    """Модель типов значений реквизитов документов"""
    req_type = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Тип значения реквизита'
    )

    objects = models.Manager()

    def __str__(self):
        return self.req_type

    class Meta:
        verbose_name = 'Тип значения реквизита'
        verbose_name_plural = 'Типы значений реквизитов'


class DocTemplateRequisites(models.Model):
    """Модель реквизитов документов"""
    req_type = models.ForeignKey(
        DocRequisiteTypes,
        on_delete=models.CASCADE,
        default=1,
        null=False,
        blank=False,
        verbose_name='Тип значения реквизита'
    )
    requisite = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Реквизит'
    )
    tag = models.CharField(
        max_length=30,
        default='tag',
        null=False,
        blank=False,
        verbose_name='Тэг'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.req_type.req_type} - {self.requisite}'

    class Meta:
        verbose_name = 'Реквизит документа'
        verbose_name_plural = 'Реквизиты документов'


class RequisitePossibleValues(models.Model):
    """Модель возможных значений реквизита (для типа значений - Выпадющий список)"""
    requisite = models.ForeignKey(
        DocTemplateRequisites,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Реквизит'
    )
    possible_value = models.CharField(
        max_length=200,
        verbose_name='Возможное значение'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.requisite.requisite} : {self.possible_value}'

    class Meta:
        verbose_name = 'Возможное значение реквизита'
        verbose_name_plural = 'Возможные значения реквизитов'
        unique_together = ('requisite_id', 'possible_value')


class DocTemplates(models.Model):
    """Модель шаблонов документов"""
    category = models.OneToOneField(
        DocTypeCategories,
        on_delete=models.CASCADE,
        verbose_name='Категория типа документа'
    )
    date_create = models.DateField(
        default=datetime.date.today,
        verbose_name='Дата создания шаблона'
    )
    name = models.TextField(
        max_length=1500,
        default='Шаблон',
        verbose_name='Наименование шаблона'
    )
    requisites = models.ManyToManyField(
        DocTemplateRequisites,
        verbose_name='Реквизиты'
    )
    doc = models.FileField(
        upload_to=DocTemplateUploadPath,
        max_length=5000,
        verbose_name='Шаблон документа'
    )

    objects = models.Manager()

    def __str__(self):
        return f'Шаблон документа типа "{self.category.type.type}" категории "{self.category.category}"'

    class Meta:
        verbose_name = 'Шаблон документа'
        verbose_name_plural = 'Шаблоны документов'


class DocTemplatePoints(models.Model):
    """Модель пунктов шаблона документа"""
    template = models.ForeignKey(
        DocTemplates,
        on_delete=models.CASCADE,
        default=1,
        blank=False,
        null=False,
        verbose_name='Шаблон'
    )
    point = models.CharField(
        max_length=300,
        verbose_name='Пункт шаблона'
    )
    tag = models.CharField(
        max_length=50,
        verbose_name='Тэг пункта шаблона'
    )

    objects = models.Manager()

    def __str__(self):
        return f'Пункт "{self.point}" шаблона "{self.template.doc.filename}"'

    class Meta:
        verbose_name = 'Пункт шаблона документа'
        verbose_name_plural = 'Пункты шаблонов документов'
        unique_together = ('template', 'tag')




