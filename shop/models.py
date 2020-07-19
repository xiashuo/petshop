from django.db import models
from user.models import *


# Create your models here.

# 订单表
class Order(models.Model):
    order_status_choices = (
        (-1, '交易取消'),
        (0, '等待付款'),
        (1, '未发货'),
        (2, '已发货'),
        (3, '已完成')
    )

    payment_method_choices = (
        (0, '支付宝'),
        (1, '微信'),
    )
    o_id = models.CharField('订单编号', max_length=50, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_time = models.DateTimeField('下单时间', auto_now_add=True)
    order_status = models.IntegerField('订单状态', choices=order_status_choices, default=0)
    order_completion_time = models.DateTimeField('订单完成时间', null=True)
    payment_method = models.IntegerField('支付方式', choices=payment_method_choices, default=0)
    shipping_address = models.CharField('收货地址', max_length=100, null=True)
    user_reviews = models.CharField('用户评价', max_length=300, null=True)
    store_reply = models.CharField('商家回评', max_length=300, null=True)

    def __str__(self):
        return f'订单编号：{self.o_id},下单时间：{self.order_time},订单状态：{self.order_status}'


class PetCategory(models.Model):
    category_name = models.CharField('宠物类别', max_length=50, unique=True)


class PetVariety(models.Model):
    pv_name = models.CharField('宠物品种', max_length=50, unique=True)
    foster_daily_price = models.DecimalField('寄养价格/天', max_digits=5, decimal_places=2)
    pet_category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'品种名称:{self.pv_name}, 寄养价格/天:{self.foster_daily_price}'


class PetProduct(models.Model):
    pet_category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    pp_name = models.CharField('商品名称', max_length=50, unique=True)
    pp_descripe = models.CharField('商品描述', max_length=200, default='暂无描述')
    pp_price = models.DecimalField('商品价格', max_digits=7, decimal_places=2)
    pp_quantity = models.IntegerField('库存数量')
    pp_image_path = models.ImageField('商品图片', null=True)
    is_featured_products = models.BooleanField('特色产品', default=0)

    def __str__(self):
        return f'商品名称：{self.pp_name},商品描述：{self.pp_descripe},商品价格：{self.pp_price},库存：{self.pp_quantity}'


class Pet(models.Model):
    pet_variety = models.ForeignKey(PetVariety, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    p_name = models.CharField('宠物名', max_length=50)
    p_describe = models.CharField('宠物描述', max_length=300, default='暂无描述')
    p_price = models.DecimalField('宠物价格', max_digits=9, decimal_places=2)
    p_image = models.ImageField('宠物照片', null=True)

    def __str__(self):
        return f'宠物名:{self.p_name}, 宠物描述:{self.p_describe}, 价格:{self.p_price}'


# 优惠码表
class CouponCode(models.Model):
    code = models.CharField('优惠码', max_length=50)
    discount = models.DecimalField('折扣', max_digits=3, decimal_places=2)
    is_effective = models.BooleanField('是否有效', default=1)


# 订单商品表
class OrderProduct(models.Model):
    # 订单
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pet_product = models.ForeignKey(PetProduct, on_delete=models.CASCADE)
    # 购买数量
    purchase_quantity = models.IntegerField('购买数量')

    def __str__(self):
        return f'{self.order}, {self.pet_product}, 数量:{self.purchase_quantity}'


# 用户购物车商品表
class UserCartProduct(models.Model):
    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 添加的商品
    pet_product = models.ForeignKey(PetProduct, on_delete=models.CASCADE)
    # 添加该商品的数量
    quantity = models.IntegerField('数量')

    def __str__(self):
        return f'商品编号：{self.pet_product_id},商品名称:{self.pet_product.pp_name},数量：{self.quantity}'


# 宠物寄养订单表
class PetFosterOrder(models.Model):
    # 订单号
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # 寄养的宠物品种
    pet_variety = models.ForeignKey(PetVariety, on_delete=models.CASCADE)
    # 该品种寄养数量
    quantity = models.IntegerField('寄养数量')
    start_date = models.DateField('寄养开始日期')
    end_date = models.DateField('寄养结束日期')

    def __str__(self):
        return f'{self.order}, {self.pet_variety}, 数量:{self.quantity}, 开始时间:{self.start_date},' \
               f' 结束时间:{self.end_date}'


# 商品收藏表
class ProductFavorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_product = models.ForeignKey(PetProduct, on_delete=models.CASCADE)


# 宠物收藏表
class PetFavorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
