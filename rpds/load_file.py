#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from rpds.header import Header
from rpds.item import Item


def load_file(file: str):
    """Loads a given file."""
    with open(file, "r") as file_open:
        header_list = []
        for line in file_open.readlines():
            line = line.strip("\n")
            if line.strip(" ").startswith("[") and line.endswith("]"):
                # The line is a header
                # print("Header: {}".format(line.strip(" ")))
                header_name = line[line.index("name=") + 5:line.index(line[-1])]
                if "," in header_name:
                    header_name = header_name[0:header_name.index(",")]
                # print("Header Name: {}".format(header_name))
                try:
                    header_type = line[line.index("type=") + 5:line.index(line[-1])]
                except ValueError:
                    header_type = "<string>"
                header = Header(header_name, header_type)
                # print("Header Type: {}".format(header_type))
                # print("-----------------------------------------------------------------------------------------------")
            elif line.strip(" ").startswith("-"):
                # The line is an item
                # print("Item: {}".format(line.strip(" ")))
                try:
                    item_key = line[line.index('"') + 1:line.find('"', line.index('"') + 1)]
                except ValueError:
                    item_key = header_name
                # print("Item Key: {}".format(item_key))
                try:
                    item_type = line[line.index("<"):line.index(">") + 1]
                except ValueError:
                    item_type = header_type
                # print("Item Type: {}".format(item_type))
                first = line.find(":")
                second = line.find(":", first + 1)
                if second == -1:
                    item_value = line[first + 2:line.index(line[-1]) + 1].strip(" ")
                else:
                    item_value = line[second + 2:line.index(line[-1]) + 1].strip(" ")
                # The item value will null if the key contains an "e" or numbers, not sure why this happens.
                item = Item(item_key, item_type, item_value)
                header.items.append(item)
                # print("Item Value: {}".format(item_value))
                # print("-----------------------------------------------------------------------------------------------")
            header_list.append(header)
    # for header in header_list:
    #     print(header.name, header.data_type)
    #     print("-------------------")
    #     for item in header.items:
    #         print(item.key, item.data_type, item.value)
    #     print("-----------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    load_file("keys.rpds")
