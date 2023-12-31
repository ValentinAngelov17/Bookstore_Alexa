# Generated by Django 4.2.3 on 2023-08-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeSupplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplies', models.CharField(choices=[('scissors', 'ножици'), ('pens', 'химикалки'), ('pencil', 'моливи'), ('corrector', 'коректори'), ('folder', 'папки'), ('tape', 'тикса'), ('glue', 'лепила')], max_length=100)),
                ('name', models.CharField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='office_covers/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
