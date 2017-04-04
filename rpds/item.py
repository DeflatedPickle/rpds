#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""


class Item(object):
    def __init__(self, key: str, data_type: str, value: str):
        self.key = key
        self.data_type = data_type
        self.value = value
