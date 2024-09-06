from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Goods, Orders, Situation, Detail

# 1. UserSerializer - 비밀번호 해싱 추가
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'login_id', 'username', 'userpwd']
        extra_kwargs = {'userpwd': {'write_only': True}}  # 비밀번호를 write-only로 설정

    def create(self, validated_data):
        validated_data['userpwd'] = make_password(validated_data['userpwd'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'userpwd' in validated_data:
            validated_data['userpwd'] = make_password(validated_data['userpwd'])
        return super().update(instance, validated_data)


# 2. GoodsSerializer
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['goods_id', 'goodsName', 'category', 'brand', 'goodsDesc', 'goodsImg', 'price', 'discountPrice']


# 3. OrdersSerializer
class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    item = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all())

    class Meta:
        model = Orders
        fields = ['order_id', 'user', 'item', 'itemCnt', 'itemPrice', 'totalPrice']


# 4. SituationSerializer
class SituationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situation
        fields = ['situation_id', 'situationCategory', 'situation', 'keyword', 'headline']


# 5. DetailSerializer
class DetailSerializer(serializers.ModelSerializer):
    situation = serializers.PrimaryKeyRelatedField(queryset=Situation.objects.all())

    class Meta:
        model = Detail
        fields = ['detail_id', 'situation', 'detail']
