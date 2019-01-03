#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers
from .models import UserFav
from rest_framework.validators import UniqueTogetherValidator


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        # ToDo items belong to a parent list, and have an ordering defined
        # by the 'position' field. No two items in a given list may share
        # the same position.
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message=("已经收藏")
            )
        ]
        fields = ("user", "goods", "id")
