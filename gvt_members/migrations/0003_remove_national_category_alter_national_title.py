# Generated by Django 4.1 on 2022-11-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvt_members', '0002_national_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='national',
            name='category',
        ),
        migrations.AlterField(
            model_name='national',
            name='title',
            field=models.CharField(choices=[('President', 'President'), ('Deputy President', 'Deputy President'), ('Cabinet Secretary', 'Cabinet Secretary')], max_length=200, null=True),
        ),
    ]