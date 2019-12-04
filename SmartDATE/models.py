from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Personne(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    naissance = models.CharField(max_length=200,
                             blank=True,null=True,
                             default='(no title)')
    description = models.TextField(blank=True,
                                   null=True,
                                   default=None)
    tags = models.ManyToManyField("Tag", related_name="Personne", blank=False)

    def __str__(self):
        return '{} ({})'.format(self.user, ' / '.join([str(c) for c in self.tags.all()]))


class Tag(models.Model):
    description = models.CharField(max_length=200,
                             blank=True,null=True,
                             default='(no title)')
    categories = models.ManyToManyField("Categorie", related_name="Tag", blank=False)

    def __str__(self):
        return '{} {}'.format(
            self.description,
            '/'.join([str(c) for c in self.categories.all()]))



class Categorie(models.Model):
    description = models.CharField(max_length=200,
                             blank=True,null=True,
                             default='(no title)')

    def __str__(self):
        return f'{str(self.description)}'