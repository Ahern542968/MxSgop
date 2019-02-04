"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin

from django.urls import path, include, re_path
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from goods.views import GoodsListViewSet, GoodsCategoryViewSet
from users.views import SmsCodeViewSet, UserRegViewSet
from user_operation.views import UserFavViewSet, UserLeavingMessageViewSet, UserAddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AlipayView


router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
# 配置category的url
router.register(r'categorys', GoodsCategoryViewSet, base_name='categorys')
# 配置验证码的url
router.register(r'code', SmsCodeViewSet, base_name='code')
# 配置注册的url
router.register(r'users', UserRegViewSet, base_name='users')
# 配置收藏的url
router.register(r'userfavs', UserFavViewSet, base_name='userfavs')
# 配置留言的url
router.register(r'messages', UserLeavingMessageViewSet, base_name='messages')
# 配置收货地址的url
router.register(r'address', UserAddressViewSet, base_name='address')
# 配置购物车的url
router.register(r'shopcarts', ShoppingCartViewSet, base_name='shopcarts')
# 配置订单的url
router.register(r'orders', OrderViewSet, base_name='orders')

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # drf自带的token认证模式
    path(r'api-token-auth/', obtain_auth_token),
    # jwt的认证接口
    path(r'login/', obtain_jwt_token),
    path(r'alipay/return/', AlipayView.as_view(), name='alipay'),
    path(r'docs/', include_docs_urls(title='慕学生鲜')),
    path(r'', include(router.urls)),
]
