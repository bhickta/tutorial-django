from django.db import models
from django.utils.translation import gettext_lazy as _

class question(models.Model):
    question = models.TextField(null=False)
    a = models.CharField(max_length=200, null=False)
    b = models.CharField(max_length=200, null=False)
    c = models.CharField(max_length=200, null=False)
    d = models.CharField(max_length=200, null=False)
    e = models.CharField(max_length=200, null=False)
    answer = models.CharField(max_length=200, null=False)
    explaination = models.CharField(max_length=200, null=False)

ANSWER_CHOICES = (
    ("choice_1", "Answer_1"),
    ("choice_2", "Answer_2"),
    ("choice_3", "Answer_3"),
    ("choice_4", "Answer_4"),
    ("choice_5", "Answer_5"),
    ("choice_6", "Answer_6"),
   
)

class sawal(models.Model):
    sawal = models.CharField(max_length=50, unique=True, choices=ANSWER_CHOICES)
    jawab = models.CharField(max_length=50, unique=True)


class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }