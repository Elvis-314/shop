"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.urls import path
from django.conf.urls import url, include
import xadmin
from shop.settings import MEDIA_ROOT
from django.views.static import serve
from django.views.generic import TemplateView

# from goods.views import GoodsListView

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset
from goods.views import IndexCategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayViewset

from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()

# 配置Goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置注册码的url
router.register(r'code', SmsCodeViewset, base_name="code")

# 配置Category的url
router.register(r'categorys', CategoryViewset, base_name="categorys")

# 用户
router.register(r'users', UserViewset, base_name="users")

# 热搜
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")

# 收藏
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# 留言
router.register(r'messages', LeavingMessageViewset, base_name='messages')

# 收货地址
router.register(r'address', AddressViewset, base_name='address')

# 购物车
router.register(r'shopcarts', ShoppingCartViewset, base_name='shopcarts')

# 订单相关
router.register(r'orders', OrderViewset, base_name='orders')

# 轮播图
router.register(r'banners', BannerViewset, base_name='banners')

# 首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, base_name='indexgoods')

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),

    # drf自带的token认证模式
    url(r'^api-auth/', include('rest_framework.urls')),

    # 获取token的url
    url(r'^api-token-auth/', views.obtain_auth_token),

    # 首页
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),

    # jwt的认证接口
    url(r'^login/$', obtain_jwt_token),

    # 富文本相关url
    # path('ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 商品列表页
    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title='商店平台')),

    url(r'^alipay/return/', AlipayViewset.as_view(), name="alipay"),

    # 第三方登录url
    url('', include('social_django.urls', namespace='social')),
]
