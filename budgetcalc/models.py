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
    optiongroup = models.ForeignKey(Optiongroup, null=True, blank=True, default=1)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = _('Option')
        verbose_name_plural = _('Options')
        ordering = ['order']

    def __unicode__(self):
        return "%s: %s" % (self.optiongroup, self.title)


class Submission(models.Model):
    """
    Selected options  and budget (filled) per email address.
    """

    email = models.EmailField()
    budget = models.FloatField('Budget gap', default=0)
    options = models.ManyToManyField(Option, null=True, blank=True, related_name='selected_options')

    class Meta:
        verbose_name = _('Submission')
        verbose_name_plural = _('Submissions')

    def __unicode__(self):
        return self.email
    

    

    