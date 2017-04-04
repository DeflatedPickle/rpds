#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""


class Header(object):
    def __init__(self, name: str, data_type: str):
        self.name = name
        self.data_type = data_type
        self.items = []
