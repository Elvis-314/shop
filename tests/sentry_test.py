#!/usr/bin/env python
# encoding: utf-8
from raven import Client

dsn = "https://2997adab286d4a10a24c5ca86cc6a648:c7aac2230b3948b2bf33e973997cf4eb@sentry.io/1368162"
client = Client(dsn)

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
