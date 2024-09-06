from rest_framework import viewsets
from .models import User, Goods, Orders, Situation, Detail
from .serializers import UserSerializer, GoodsSerializer, OrdersSerializer, SituationSerializer, DetailSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class SituationViewSet(viewsets.ModelViewSet):
    queryset = Situation.objects.all()
    serializer_class = SituationSerializer


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
