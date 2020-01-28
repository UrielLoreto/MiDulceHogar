
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name='product-all'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('getbyname', ProductGeyByName.as_view(), name='product-byname'),
    path('getbyid/<int:id>/', ProductGeyById.as_view(), name='product-byid'),
    path('<int:id>/updateprice/', ProducUpdatePriceView.as_view(), name='product-updateprice'),
    path('<int:id>/updatedesc/', ProducUpdateDescriptionView.as_view(), name='product-updatedesc'),
    path('<int:id>/delete/', ProducDeletetView.as_view(), name='product-delete'),
    path('buy/log/', SaleView.as_view(), name='product-log'),
    path('buy/', SaleCreateView.as_view(), name='product-buy'),
]
