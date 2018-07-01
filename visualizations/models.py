from django.db import models

# Create your models here.


class HousingCompletion(models.Model):
    label = models.CharField(max_length=120)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class ReconstructionGrant(models.Model):
    label = models.CharField(max_length=120)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class RecentStory(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='recentstories/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
