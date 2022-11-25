from django.db import models

class National(models.Model):
    CATEGORY = (
        ('Presidential', 'Presidential'),
        ('Cabinet', 'Cabinet'),
    )
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    photo = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name


class Governors(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name

class Senators(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name

class Womenrepresentatives(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name

