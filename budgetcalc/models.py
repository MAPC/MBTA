from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

CATEGORY_TYPES = (
    ('r', 'Revenue'),
    ('s', 'Savings'),
)

class Category(models.Model):
    title = models.CharField(max_length=100)
    cat_type = models.CharField('Type', max_length=1, choices=CATEGORY_TYPES, default='r')
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['order']

    def __unicode__(self):
        return self.title


class Optiongroup(models.Model):
    """
    Grouping of options with radio buttons.
    """

    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = _('Optiongroup')
        verbose_name_plural = _('Optiongroups')

    def __unicode__(self):
        return self.title


class Option(models.Model):
    """
    Budget-options.
    """

    title = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    category = models.ForeignKey(Category, default=1)
    optiongroup = models.ForeignKey(Optiongroup, null=True, blank=True)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = _('Option')
        verbose_name_plural = _('Options')
        ordering = ['order']

    def __unicode__(self):
        return self.title
    

    