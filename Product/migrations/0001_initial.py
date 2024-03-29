# Generated by Django 2.2.7 on 2019-11-22 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(blank=True, max_length=200, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Category', models.CharField(choices=[('', '_______________________Voiture _______________________'), ('Citroen', 'Citroen'), ('CATCAT', 'CATCAT'), ('Renault19', 'Renault19'), ('Dacia', 'Dacia'), ('', '_______________________Camion_______________________'), ('Camionone', 'Camionone'), ('Camiontwo', 'Camiontwo'), ('Camionthree', 'Camionthree'), ('Camionfor', 'Camionfor'), ('', '_______________________Volvo_______________________'), ('VolvoOne', 'VolvoOne'), ('VolvoTwo', 'VolvoTwo'), ('VolvoThree', 'VolvoThree'), ('Volvofor', 'Volvofor')], max_length=600)),
                ('Ville', models.CharField(choices=[('', '_______________________Ville _______________________'), ('Agadir', 'Agadir'), ('Rabat', 'Rabat'), ('Casablanca', 'Casablanca'), ('Tanger', 'Tanger')], max_length=600)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('Price', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['-Created'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height_field', models.IntegerField(default=600, null=True)),
                ('width_field', models.IntegerField(default=600, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagess', to='Product.Product')),
            ],
        ),
    ]
