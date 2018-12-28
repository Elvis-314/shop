#!/usr/bin/env python
# encoding: utf-8

import json
import requests


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.sigle_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【dbshop商城】您的验证码是#code#。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.sigle_send_url, data=params)
        re_dict = json.loads(response.text)
        print(re_dict)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("3e9f9b74636cc8e492a4988b64626aab")
    yun_pian.send_sms("2018", "13880037335")
