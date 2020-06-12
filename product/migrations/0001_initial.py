# Generated by Django 2.2.13 on 2020-06-07 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=100, null=True)),
                ('region', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=500)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_main', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('image_6', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
    ]
