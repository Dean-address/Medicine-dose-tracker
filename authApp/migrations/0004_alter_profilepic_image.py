# Generated by Django 5.1.1 on 2024-10-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_alter_profilepic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
