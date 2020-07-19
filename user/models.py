from django.db import models

# Create your models here.
# 用户表
class User(models.Model):
    sex_choices = [
        ('m', '男'),
        ('f', '女'),
        ('o', '其他')
    ]
    user_name = models.CharField('昵称', max_length=50, unique=True)
    password = models.CharField('密码', max_length=50)
    phone_number = models.CharField('手机号', max_length=50, unique=True)
    register_time = models.DateField('注册时间', auto_now_add=True)
    email = models.EmailField('邮箱', max_length=50, null=True)
    real_name = models.CharField('真实姓名', max_length=50, null=True)
    id_card = models.CharField('身份证', max_length=50, null=True)
    sex = models.CharField('性别', max_length=50, choices=sex_choices, default='m')
    birthday = models.DateField('生日', null=True)
    last_login_time = models.DateTimeField('上次登录时间', null=True)


# 收货地址表
class ShippingAddress(models.Model):
    receiver_name = models.CharField('收货人', max_length=50)
    address = models.CharField('收货地址', max_length=100)
    postcode = models.CharField('邮编', max_length=50, null=True)
    receiver_phone_number = models.CharField('收货人手机号', max_length=50)
    is_default = models.BooleanField('默认地址', default=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'收货人：{self.receiver_name}，收货地址：{self.address}，电话：{self.receiver_phone_number}'


# 用户反馈表
class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_content = models.CharField('反馈内容', max_length=300)
    feedback_time = models.DateTimeField('反馈时间', auto_now_add=True)
    store_reply = models.CharField('店家回复', max_length=300, null=True)
    reply_time = models.DateTimeField('回复时间', null=True)

    def __str__(self):
        return f'编号:{self.user_id},反馈内容:{self.feedback_content},反馈时间:' \
               f'{self.feedback_time},店家回复:{self.store_reply},回复时间:{self.reply_time}'


# 消息表
class Message(models.Model):
    # 消息接受对象
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    m_content = models.CharField('消息内容', max_length=300)
    m_time = models.DateTimeField('发送时间', auto_now_add=True)
    m_status = models.BooleanField('已读/未读', default=0)

    def __str__(self):
        return f'消息内容:{self.m_content}, 发送时间:{self.m_time}, ' \
               f'消息状态:{self.m_status}'


# 全站消息表
class StationNews(models.Model):
    sn_content = models.CharField('全站消息内容', max_length=300)
    sn_time = models.DateTimeField('发布时间', auto_now_add=True)
