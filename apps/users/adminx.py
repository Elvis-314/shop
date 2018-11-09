#!/usr/bin/env python
# encoding: utf-8

import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_theme = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '商品后台管理'
    site_footer = '我的商店'


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
