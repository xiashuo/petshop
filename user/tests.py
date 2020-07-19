from django.test import TestCase
from .models import *
from shop.models import *


# Create your tests here.
class TestDatabases(TestCase):
    # 测试所有表的级联关系
    def test_tables(self):
        '''
        测试用户与收货地址的一对多关系
        '''
        # 插入用户表数据和收货地址表数据,
        for i in range(1, 6):
            User.objects.create(id=i, user_name=f'xiashuo{i}', password='135456..', phone_number=f'1567155925{i}')
            ShippingAddress.objects.create(receiver_name=f'张三{i}', address='广东,深圳,龙华',
                                           receiver_phone_number='1383838438', user_id=i)
            ShippingAddress.objects.create(receiver_name=f'李四{i}', address='广东,深圳,龙华',
                                           receiver_phone_number='1383838438', user_id=i)
        # 显示某个用户的所有收货地址
        for i in range(1, 6):
            print(f'id为{i}的用户的所有收货地址如下：')
            addresses = ShippingAddress.objects.filter(user_id=i)
            for addr in addresses:
                print(addr)
        print()

        '''
        测试用户与订单一对多关系
        '''
        # 插入订单表数据
        for i in range(1, 6):
            Order.objects.create(o_id=f'{i}20200719132400', user_id=i)
            Order.objects.create(o_id=f'{i}20200719132405', user_id=i)

        # 显示某个用户的所有订单
        for i in range(1, 6):
            print(f'编号为{i}的用户的所有订单如下：')
            orders = Order.objects.filter(user_id=i)
            for order in orders:
                print(order)
        print()

        '''
        测试宠物分类与宠物商品的一对多关系
        '''
        # 插入宠物商品表和宠物分类表数据,
        for i in range(1, 6):
            PetCategory.objects.create(category_name=f'类别{i}')
            PetProduct.objects.create(pet_category_id=i, pp_name=f'商品1_{i}', pp_price=23, pp_quantity=50)
            PetProduct.objects.create(pet_category_id=i, pp_name=f'商品2_{i}', pp_price=22, pp_quantity=50)
        # 显示某个分类下的所有宠物商品,例如显示类别1.
        pc = PetCategory.objects.get(category_name='类别1')
        pps = PetProduct.objects.filter(pet_category=pc)
        print('\n类别1下所有商品如下：')
        for pp in pps:
            print(pp)

        '''
        测试用户与购物车商品的多对多关系
        '''
        # 插入购物车商品表数据
        for i in range(1, 5):
            UserCartProduct.objects.create(user_id=i, pet_product_id=i, quantity=1)
            UserCartProduct.objects.create(user_id=i, pet_product_id=i + 1, quantity=2)
            UserCartProduct.objects.create(user_id=i + 1, pet_product_id=i, quantity=1)
            UserCartProduct.objects.create(user_id=i + 1, pet_product_id=i + 1, quantity=1)

        # 显示id为1的用户的购物车清单
        cps = UserCartProduct.objects.filter(user_id=1)
        print('\nid为1的用户的购物车清单:')
        for cp in cps:
            print(cp)

        '''
        测试用户与反馈信的一对多关系
        '''
        # 插入反馈表数据
        for i in range(1, 6):
            UserFeedback.objects.create(user_id=i, feedback_content=f'反馈内容1{i}')
            UserFeedback.objects.create(user_id=i, feedback_content=f'反馈内容2_{i}')

        # 显示用户编号为3的所有反馈信
        user_feedbacks = UserFeedback.objects.filter(user_id=3)
        print('\n编号为3的的用户的所有反馈信如下:')
        for ufb in user_feedbacks:
            print(ufb)

        '''
        测试用户与消息的一对多关系
        '''
        # 插入消息表数据
        for i in range(1, 6):
            Message.objects.create(user_id=i, m_content=f'消息1_{i}')
            Message.objects.create(user_id=i, m_content=f'消息2_{i}')
        # 显示某个用户收到的所有消息,如编号为3的用户
        print('\n编号为3的用户的所有接收消息如下:')
        messeges = Message.objects.filter(user_id=3)
        for msg in messeges:
            print(msg)

        '''
        测试宠物类别与宠物品种的一对多关系
        '''
        # 插入宠物品种表数据
        for i in range(1, 6):
            PetVariety.objects.create(pv_name=f'类别{i}-品种1_{i}', foster_daily_price=50,
                                      pet_category_id=i)
            PetVariety.objects.create(pv_name=f'类别{i}-品种2_{i}', foster_daily_price=50,
                                      pet_category_id=i)
        # 显示某个宠物大类下的所有品种,如类别3
        print('\n编号为3的宠物大类下的所有品种如下:')
        varieties = PetVariety.objects.filter(pet_category_id=3)
        for variety in varieties:
            print(variety)

        '''
        测试宠物品种与宠物的一对多关系
        '''
        # 插入宠物表数据
        for i in range(1, 6):
            Pet.objects.create(pet_variety_id=i, p_name=f'宠物a_{i}', p_price=2000)
            Pet.objects.create(pet_variety_id=i, p_name=f'宠物b_{i}', p_price=1000)
        # 显示某个品种下的所有宠物,品种编号为2
        print('\n品种编号为2下的所有宠物为:')
        pets = Pet.objects.filter(pet_variety_id=2)
        for pet in pets:
            print(pet)
        '''
        测试用户与收藏夹商品的多对多关系
        '''
        # 插入商品收藏表数据
        pf1 = ProductFavorites.objects.create(user_id=1, pet_product_id=1)
        pf2 = ProductFavorites.objects.create(user_id=1, pet_product_id=2)
        pf3 = ProductFavorites.objects.create(user_id=2, pet_product_id=1)
        pf4 = ProductFavorites.objects.create(user_id=2, pet_product_id=2)
        # 显示某个用户的收藏的所有商品,如用户编号为2
        print('\n编号为2的用户收藏的所有商品如下:')
        pfs = ProductFavorites.objects.filter(user_id=2)
        for pf in pfs:
            print(pf.pet_product)

        '''
        测试用户与收藏夹宠物的多对多关系
        '''
        # 插入宠物收藏表数据
        pf1 = PetFavorites.objects.create(user_id=1, pet_id=1)
        pf2 = PetFavorites.objects.create(user_id=1, pet_id=2)
        pf3 = PetFavorites.objects.create(user_id=2, pet_id=1)
        pf4 = PetFavorites.objects.create(user_id=2, pet_id=2)
        # 显示某个用户的收藏的所有宠物,如用户编号为1
        print('\n编号为1的用户收藏的所有宠物如下:')
        pfs = PetFavorites.objects.filter(user_id=2)
        for pf in pfs:
            print(pf.pet)

        '''
        测试宠物品种与宠物寄养订单的多对多关系
        '''
        # 插入宠物寄养订单表数据
        PetFosterOrder.objects.create(order_id='120200719132400', pet_variety_id=1, quantity=1,
                                      start_date='2020-07-20', end_date='2020-07-25')
        PetFosterOrder.objects.create(order_id='120200719132400', pet_variety_id=2, quantity=1,
                                      start_date='2020-07-20', end_date='2020-07-25')
        PetFosterOrder.objects.create(order_id='220200719132400', pet_variety_id=1, quantity=1,
                                      start_date='2020-07-20', end_date='2020-07-25')
        PetFosterOrder.objects.create(order_id='220200719132400', pet_variety_id=2, quantity=1,
                                      start_date='2020-07-20', end_date='2020-07-25')

        # 显示某个用户的寄养订单,如用户编号为1
        print('\n编号为1的用户的寄养订单如下:')
        pfos = PetFosterOrder.objects.filter(order__user_id=1)
        for pfo in pfos:
            print(pfo)

        '''
        测试订单与商品的多对多
        '''
        # 插入订单商品表数据
        OrderProduct.objects.create(order_id='120200719132405', pet_product_id=1, purchase_quantity=1)
        OrderProduct.objects.create(order_id='120200719132405', pet_product_id=2, purchase_quantity=1)
        OrderProduct.objects.create(order_id='220200719132405', pet_product_id=1, purchase_quantity=1)
        OrderProduct.objects.create(order_id='220200719132405', pet_product_id=2, purchase_quantity=1)

        # 显示某个用户的商品订单详细信息,如编号为2的用户
        print('\n编号为2的用户的所有商品订单如下:')
        ops = OrderProduct.objects.filter(order__user_id=2)
        for op in ops:
            print(op)

        '''
        订单与领养的宠物的一对多
        '''
        # 显示某个用户的所有领养宠物订单,如用户编号为3
        print('\n编号为3的用户的所有领养订单如下:')
        Pet.objects.create(pet_variety_id=1, order_id='320200719132405',
                           p_name='火箭', p_price=5000)
        Pet.objects.create(pet_variety_id=2, order_id='320200719132405',
                           p_name='蛋饼', p_price=7000)
        pets = Pet.objects.filter(order__user_id=3)
        for pet in pets:
            print(f'{pet.order},{pet}')
