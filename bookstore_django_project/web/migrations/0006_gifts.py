# Generated by Django 4.2.3 on 2023-08-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_officesupplies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('gifts', 'подаръци'), ('other', 'сувенири')], max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='gifts_cover/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
