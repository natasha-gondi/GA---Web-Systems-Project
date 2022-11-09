from django.db import models

class National(models.Model):
    TITLE = (
        ('President', 'President'),
        ('Deputy President', 'Deputy President'),
        ('Cabinet Secretary', 'Cabinet Secretary'),
    )
    CATEGORY = (
        ('Presidential', 'Presidential'),
        ('Cabinet', 'Cabinet'),
    )
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True, choices=TITLE)
    description = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    photo = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name