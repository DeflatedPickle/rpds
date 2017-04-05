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
                header_name = line[line.index("name=") + 5:line.index(line[-1])]
                # Sets the header name to the name found on the line.
                if "," in header_name:
                    header_name = header_name[0:header_name.index(",")]
                    # Removes anything past a comma if one is found
                try:
                    header_type = line[line.index("type=") + 5:line.index(line[-1])]
                    # Sets the header type if one is found.
                except ValueError:
                    header_type = "<string>"
                    # Sets the header type to "<string>" if none is found.
                header = Header(header_name, header_type)
                header_list.append(header)
            elif line.strip(" ").startswith("-"):
                # The line is an item
                try:
                    item_key = line[line.index('"') + 1:line.find('"', line.index('"') + 1)]
                    # Sets the items' key to the key on the line if one is found.
                except ValueError:
                    item_key = header_name
                    # Sets the items key to the headers name if no key is found.
                try:
                    item_type = line[line.index("<"):line.index(">") + 1]
                    # Sets the items type to the one on the line if one is found.
                except ValueError:
                    item_type = header_type
                    # Sets the items type to the headers type if no type is found.
                first = line.find(":")
                second = line.find(":", first + 1)
                if second == -1:
                    item_value = line[first + 2:line.index(line[-1]) + 1].strip(" ")
                    # Sets the item value if no type is found.
                else:
                    item_value = line[second + 2:line.index(line[-1]) + 1].strip(" ")
                    # Sets the item value if a type is found.
                item = Item(item_key, item_type, item_value)
                header.items.append(item)
    return header_list


if __name__ == "__main__":
    rpds_file = load_file("keys.rpds")
    for file_header in rpds_file:
        print(file_header.name)
        for header_item in file_header.items:
            print(header_item.value)
