from django.db import models
from django.contrib.auth.models import User

from stdimage.models import StdImageField
from ckeditor.fields import RichTextField
from stdimage.validators import MinSizeValidator
from django.contrib.gis.db.models import PointField
from phonenumber_field.modelfields import PhoneNumberField

MEDIA_CHOICES = (
    ("AUDIO", "Audio"),
    ("VIDEO", "Video"),
    ("IMAGE", "Image"),

)


class HousingCompletion(models.Model):
    label = models.CharField(max_length=120)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = 'Reconstruction Stages'


class ReconstructionGrant(models.Model):
    label = models.CharField(max_length=120)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = 'Reconstruction Grant'


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Districts'


class Gaunpalika(models.Model):
    district = models.ForeignKey(District, related_name='gaunpalika', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_municipality = models.BooleanField(default=False)

    def __str__(self):
        if self.district.name == 'Nuwakot':
            if self.is_municipality:
                return self.name
            else:
                return "{} Gaunpalika".format(self.name)
        else:
            if self.is_municipality:
                return "{} Municipality".format(self.name)
            return "{} Gaunpalika".format(self.name)

    class Meta:
        verbose_name_plural = 'Gaunpalika'


class Data(models.Model):

    """
    Stores a single data entry, related to :model:`District` and
    :model:`Gaunpaika`.
    """
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

    class Meta:
        verbose_name_plural = 'Reconstruction per Municipality'

    def get_version(self):
        return self.version

    @property
    def thcp(self):
        if self.total_houses == 0:
            return 0
        return round((self.houses_completed / self.total_houses) * 100, 2)

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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField("Title", max_length=255)
    description = models.CharField("subtitle", max_length=255)
    content = RichTextField()
    thumbnail = StdImageField(validators=[MinSizeValidator(100, 100)])
    banner = StdImageField(validators=[MinSizeValidator(1600, 600)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    use_banner = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Stories From The Field'


class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='event/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Events'


class Training(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='training/', blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Trainings'


class DispensedAmount(models.Model):
    amount = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name_plural = 'Disbursed Amount'


class TotalAmount(models.Model):
    amount = models.FloatField()

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name_plural = 'Total EOI Funding'


class Media(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(choices=MEDIA_CHOICES, max_length=300, default=MEDIA_CHOICES[0][0])
    file = models.FileField(upload_to='media/', null=True, blank=True)
    title = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Media'


class ProjectStakeholders(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    logo = models.ImageField(upload_to='project_stakeholders/')
    role = models.TextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Partners'


class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    content = RichTextField()

    def __str__(self):
        return self.content[:15]

    class Meta:
        verbose_name_plural = 'Project Overview'


class Contact(models.Model):
    partner_name = models.OneToOneField(ProjectStakeholders, related_name="project_stakeholders", on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    phone = PhoneNumberField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.partner_name.name

    class Meta:
        verbose_name_plural = 'Contacts'


class Materials(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    document = models.FileField(upload_to='materials/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Materials'


class STFCLocations(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    district_name = models.CharField(max_length=200, null=True, blank=True)
    latlong = PointField(null=True, blank=True)
    contact_number = models.CharField(max_length=200, null=True, blank=True)
    contact_person = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


