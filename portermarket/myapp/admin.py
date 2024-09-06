from django.contrib import admin
from .models import Goods, Orders, Situation, User, Detail

# Custom User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'login_id', 'username')  # 필드 이름에 맞게 수정
    search_fields = ('login_id', 'username')
    ordering = ('login_id',)

# Goods Admin
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('goods_id', 'goodsName', 'category', 'brand', 'price', 'discountPrice')  # 필드 이름에 맞게 수정
    search_fields = ('goodsName', 'category', 'brand')

# Orders Admin
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'item_id', 'itemCnt', 'itemPrice', 'totalPrice')  # 필드 이름에 맞게 수정
    search_fields = ('user__username',)

# Situation Admin
@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ('situation_id', 'situationCategory', 'situation', 'keyword', 'headline')  # 필드 이름에 맞게 수정
    search_fields = ('situation', 'keyword', 'headline')

# Detail Admin
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('detail_id', 'situation', 'detail')  # 필드 이름에 맞게 수정
    search_fields = ('detail',)
