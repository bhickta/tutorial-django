from django.db import models

class question(models.Model):
    question = models.TextField(null=False)
    a = models.CharField(max_length=200, null=False)
    b = models.CharField(max_length=200, null=False)
    c = models.CharField(max_length=200, null=False)
    d = models.CharField(max_length=200, null=False)
    e = models.CharField(max_length=200, null=False)
    answer = models.CharField(max_length=200, null=False)
    explaination = models.CharField(max_length=200, null=False)