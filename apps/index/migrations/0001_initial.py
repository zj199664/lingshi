# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-22 12:15
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=11)),
                ('icon', models.ImageField(default='static/image/1.jpg', upload_to='upload/img/%Y%m%d')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addr_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('detail_addr', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('nav_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=255)),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('cate_name', models.CharField(max_length=64)),
                ('is_delete', models.BooleanField(default=False)),
                ('crete_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=4000)),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('order_code', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=255)),
                ('receiver', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('pay_time', models.CharField(max_length=64)),
                ('confirm_time', models.CharField(max_length=64)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('promote_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('stock', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('car_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('shop_number', models.IntegerField()),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('shop_id', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shop_car',
            },
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('image_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('img_url', models.CharField(max_length=255)),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('shop_id', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop')),
            ],
            options={
                'db_table': 'shop_image',
            },
        ),
        migrations.CreateModel(
            name='ShopProperty',
            fields=[
                ('property_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('shop_id', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop')),
            ],
            options={
                'db_table': 'shop_property',
            },
        ),
        migrations.CreateModel(
            name='SubCate',
            fields=[
                ('sub_cate_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('cate_id', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.CASCADE, to='index.Category')),
            ],
            options={
                'db_table': 'sub_cate',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='sub_cate_id',
            field=models.ForeignKey(db_column='sub_cate_id', on_delete=django.db.models.deletion.CASCADE, to='index.SubCate'),
        ),
        migrations.AddField(
            model_name='order',
            name='car_id',
            field=models.OneToOneField(db_column='car_id', on_delete=django.db.models.deletion.CASCADE, to='index.ShopCar'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='shop_id',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='index.Shop'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]