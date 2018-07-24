from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.
from django.db.models import Sum, Count


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


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Gaunpalika(models.Model):
    district = models.ForeignKey(District, related_name='gaunpalika', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_municipality = models.BooleanField(default=False)

    def __str__(self):
        if self.is_municipality:
            return "{} Municipality".format(self.name)
        return "{} Gaunpalika".format(self.name)


class Data(models.Model):
    gaunpalika = models.ForeignKey(Gaunpalika, related_name='data', on_delete=models.CASCADE)
    houses_in_stage_i = models.PositiveIntegerField(default=0)
    houses_in_stage_ii = models.PositiveIntegerField(default=0)
    houses_in_stage_iii = models.PositiveIntegerField(default=0)
    received_tranche_i = models.PositiveIntegerField(default=0)
    received_tranche_ii = models.PositiveIntegerField(default=0)
    received_tranche_iii = models.PositiveIntegerField(default=0)
    version = models.IntegerField(null=True, blank=True)
    source_is_fieldSight = models.BooleanField(default=True)
    total_houses = models.IntegerField(default=0)
    houses_completed = models.IntegerField(default=0)
    women_percentage = models.IntegerField(default=0)

    def __str__(self):
        return "{} data".format(self.gaunpalika.name)

    def get_version(self):
        return self.version

    @property
    def thcp(self):
        if self.total_houses == 0:
            return 0
        return round((self.houses_completed / self.total_houses)*100, 2)

    @property
    def s1p(self):
        if self.total_houses == 0:
            return 0
        s1p = round((self.houses_in_stage_i / self.total_houses) * 100, 2)
        return s1p

    @property
    def s2p(self):
        if self.total_houses == 0:
            return 0
        s2p = round((self.houses_in_stage_ii / self.total_houses) * 100, 2)
        return s2p

    @property
    def s3p(self):
        if self.total_houses == 0:
            return 0
        s3p = round((self.houses_in_stage_iii / self.total_houses) * 100, 2)
        return s3p

    @property
    def t1p(self):
        if self.total_houses == 0:
            return 0
        t1p = round((self.received_tranche_i / self.total_houses) * 100, 2)
        return t1p

    @property
    def t2p(self):
        if self.total_houses == 0:
            return 0
        t2p = round((self.received_tranche_ii / self.total_houses) * 100, 2)
        return t2p

    @property
    def t3p(self):
        if self.total_houses == 0:
            return 0
        t3p = round((self.received_tranche_iii / self.total_houses) * 100, 2)
        return t3p


class RecentStories(models.Model):
    title = models.CharField("Title", max_length=20)
    description = models.CharField("Short Description", max_length=20)
    content = FroalaField()
    thumbnail = models.ImageField()
    banner = models.ImageField()


