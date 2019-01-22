from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=11)
    icon = models.ImageField(max_length=100, upload_to='upload/img/%Y%m%d', default=u'static/image/1.jpg')

    class Meta:
        db_table = 'user'


class Address(models.Model):
    addr_id = models.AutoField(primary_key=True, auto_created=True)
    detail_addr = models.CharField(max_length=255)
    # 地址表示，1代表默认地址，0代表普通地址
    status = models.BooleanField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, db_column='user_id')
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'address'


class Banner(models.Model):
    nav_id = models.AutoField(primary_key=True, auto_created=True)
    image_url = models.CharField(max_length=255)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'banner'


class Category(models.Model):
    cate_id = models.AutoField(primary_key=True, auto_created=True)
    cate_name = models.CharField(max_length=64)
    is_delete = models.BooleanField(default=False)
    crete_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'


class SubCate(models.Model):
    sub_cate_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=64)
    cate_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='cate_id', db_index=True)

    class Meta:
        db_table = 'sub_cate'


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    promote_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    quantity = models.IntegerField(default=0)
    sub_cate_id = models.ForeignKey(SubCate, on_delete=models.CASCADE, db_column='sub_cate_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop'


class ShopProperty(models.Model):
    property_id = models.AutoField(primary_key=True, auto_created=True)
    value = models.CharField(max_length=255)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_property'


class ShopCar(models.Model):
    car_id = models.AutoField(primary_key=True, auto_created=True)
    shop_number = models.IntegerField()
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_car'


class ShopImage(models.Model):
    image_id = models.AutoField(primary_key=True, auto_created=True)
    img_url = models.CharField(max_length=255)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shop_image'


class Order(models.Model):
    oid = models.AutoField(primary_key=True, auto_created=True)
    order_code = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    receiver = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    message = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.CharField(max_length=64)
    confirm_time = models.CharField(max_length=64)
    # 订单状态：-1代表删除，0代表取消，1代表支付，2代表未支付，3代表完成
    status = models.IntegerField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)
    car_id = models.OneToOneField(ShopCar, on_delete=models.CASCADE, db_column='car_id', db_index=True)

    class Meta:
        db_table = 'order'


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, auto_created=True)
    content = models.CharField(max_length=4000)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column='shop_id', db_index=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', db_index=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comment'
