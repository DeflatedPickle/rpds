#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""


class Header(object):
    def __init__(self, name: str, docstring: str, data_type: str, key: str):
        self.name = name
        self.data_type = data_type
        self.key = key
        self.items = {}
        self.docstring = docstring

    def __getitem__(self, item):
        return self.items[item]

    def __repr__(self):
        return self.name

    def item(self, item):
        return self.items[item]
