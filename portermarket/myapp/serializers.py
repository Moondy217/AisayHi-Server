from rest_framework import serializers
from .models import User, Goods, Orders, Situation, Detail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'login_id', 'username', 'userpwd']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['goods_id', 'goodsName', 'category', 'brand', 'goodsDesc', 'goodsImg', 'price', 'discountPrice']


class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    item = GoodsSerializer()

    class Meta:
        model = Orders
        fields = ['order_id', 'user', 'item', 'itemCnt', 'itemPrice', 'totalPrice']


class SituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situation
        fields = ['situation_id', 'situationCategory', 'situation', 'keyword', 'headline']


class DetailSerializer(serializers.ModelSerializer):
    situation = SituationSerializer()

    class Meta:
        model = Detail
        fields = ['detail_id', 'situation', 'detail']
