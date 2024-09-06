from django.db import models

# 1) 회원 테이블
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=20)
    userpwd = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

# 2) 상품 테이블
class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goodsName = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    goodsDesc = models.TextField(null=True, blank=True)
    goodsImg = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    discountPrice = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'goods'
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'

    def __str__(self):
        return self.goodsName

# 3) 주문 테이블
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.IntegerField()
    itemCnt = models.IntegerField()
    itemPrice = models.IntegerField()
    totalPrice = models.IntegerField()

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.order_id} by {self.user.username}'

# 4) 상황 테이블
class Situation(models.Model):
    situation_id = models.AutoField(primary_key=True)
    situationCategory = models.CharField(max_length=50)
    situation = models.CharField(max_length=30)
    keyword = models.CharField(max_length=30)
    headline = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'situation'
        verbose_name = 'Situation'
        verbose_name_plural = 'Situations'

    def __str__(self):
        return self.headline

# 5) 세부 항목 테이블
class Detail(models.Model):
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE)
    detail_id = models.AutoField(primary_key=True)
    detail = models.CharField(max_length=150)

    class Meta:
        db_table = 'detail'
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'

    def __str__(self):
        return self.detail
