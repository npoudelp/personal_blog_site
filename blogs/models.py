from django.db import models
from tinymce import models as mce_model


# Create your models here.


class post(models.Model):

    AUTHORS = [
        ('npoudelp', 'npoudelp'),
        ('bqtbsb', 'bqtbsb'),
    ]

    STAT = [
        ('draft', 'draft'),
        ('publish', 'publish'),
    ]

    thumbnail = models.ImageField(blank=True, null=True)
    author = models.CharField(choices=AUTHORS, max_length=25)
    title = models.CharField(max_length=255)
    blog = mce_model.HTMLField(null=True, blank=True)
    date = models.DateField()   
    tags = models.CharField(max_length=25, default='Empty')
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STAT, max_length=25, default='draft')

    def __str__(self):
        return f'{self.title} -> {self.status}'
