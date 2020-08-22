# Generated by Django 3.1 on 2020-08-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceWatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=30, verbose_name='Province')),
                ('entryDate', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('NFA', models.CharField(max_length=30)),
                ('Imported_Special', models.CharField(max_length=30)),
                ('Imported_Premium', models.CharField(max_length=30)),
                ('Imported_Well_milled', models.CharField(max_length=30)),
                ('Imported_Regular_milled', models.CharField(max_length=30)),
                ('Local_Special', models.CharField(max_length=30)),
                ('Local_Premium', models.CharField(max_length=30)),
                ('Local_Well_milled', models.CharField(max_length=30)),
                ('Local_Regular_milled', models.CharField(max_length=30)),
                ('Bangus', models.CharField(max_length=30)),
                ('Tilapia', models.CharField(max_length=30)),
                ('Local_Galunggong', models.CharField(max_length=30)),
                ('Imported_Galunggong', models.CharField(max_length=30)),
                ('Alumahan', models.CharField(max_length=30)),
                ('Ampalaya', models.CharField(max_length=30)),
                ('Sitao', models.CharField(max_length=30)),
                ('Squash', models.CharField(max_length=30)),
                ('Eggplant', models.CharField(max_length=30)),
                ('Tomato', models.CharField(max_length=30)),
                ('Cabbage', models.CharField(max_length=30)),
                ('Carrots', models.CharField(max_length=30)),
                ('Habitchuelas', models.CharField(max_length=30)),
                ('White_Potato', models.CharField(max_length=30)),
                ('Pechay', models.CharField(max_length=30)),
                ('Chayote', models.CharField(max_length=30)),
                ('Local_Red_Onion', models.CharField(max_length=30)),
                ('Imported_Red_Onion', models.CharField(max_length=30)),
                ('Local_White_Onion', models.CharField(max_length=30)),
                ('Imported_White_Onion', models.CharField(max_length=30)),
                ('Local_Garlic', models.CharField(max_length=30)),
                ('Imported_Garlic', models.CharField(max_length=30)),
                ('Ginger', models.CharField(max_length=30)),
                ('Chili', models.CharField(max_length=30)),
                ('Calamansi', models.CharField(max_length=30)),
                ('Banana_Lakatan', models.CharField(max_length=30)),
                ('Banana_Latundan', models.CharField(max_length=30)),
                ('Papaya', models.CharField(max_length=30)),
                ('Mango', models.CharField(max_length=30)),
            ],
        ),
    ]
