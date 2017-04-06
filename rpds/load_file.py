#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

from rpds.header import Header
from rpds.item import Item


def load_file(file: str):
    """Loads a given file."""
    with open(file, "r") as file_open:
        header_list = {}
        header_name = None
        header_docstring = ""
        header_type = None
        header = None
        header_key = None
        header_count = 0
        for line in file_open.readlines():
            line = line.strip("\n")
            if line.strip(" ").startswith("[") and line.endswith("]"):
                # The line is a header.
                header_count = 0
                header_name = line[line.index("name=") + 5:line.index(line[-1])]
                # Sets the header name to the name found on the line.
                if ", type=" in header_name:
                    header_name = header_name[0:header_name.index(", type=")]
                    # Removes the type from the name if found.
                try:
                    header_type = line[line.index("type=") + 5:line.index(line[-1])]
                    # Sets the header type if one is found.
                except ValueError:
                    header_type = "<string>"
                    # Sets the header type to "<string>" if none is found.
                if ", key=" in header_name:
                    header_name = header_name[0:header_name.index(", key=")]
                    # Removes the key from the name if found.
                elif ", key=" in header_type:
                    header_type = header_type[0:header_type.index(", key=")]
                    # Removes the key from the type if found.
                try:
                    header_key = line[line.index("key=") + 4:line.index(line[-1])]
                    # Sets the key type if one is found.
                except ValueError:
                    header_key = "<count>"
                    # Sets the key to "<count>" if none is found.
                header = Header(header_name, header_docstring, header_type, header_key)
                header_list[header_name] = header
            elif line.strip(" ").startswith('"""') and line.endswith('"""'):
                # This line is a docstring.
                header.docstring = line[3:-3]
            elif line.strip(" ").startswith("-"):
                # The line is an item.
                try:
                    item_key = line[line.index('"') + 1:line.find('"', line.index('"') + 1)]
                    # Sets the items' key to the key on the line if one is found.
                except ValueError:
                    if header_key == "<count>":
                        item_key = str(header_count)
                        header_count += 1
                        # Sets the item's key to a counting number if no key is found and the headers key is "<count">
                    else:
                        item_key = header_name
                        # Sets the item's key to the headers name if no key is found.
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
                item_comment = None
                if "//" in item_value:
                    # Removes a C-style comment if one is found.
                    item_comment = item_value[item_value.index("//") + 2:line.index(line[-1]) + 1].strip(" ")
                    item_value = item_value[0:item_value.index("//")]
                if "#" in item_value:
                    # Removes a Python-style comment if one is found.
                    item_comment = item_value[item_value.index("#") + 1:line.index(line[-1]) + 1].strip(" ")
                    item_value = item_value[0:item_value.index("#")]
                item = Item(item_key, item_type, item_value, item_comment)
                header.items[item_key] = item
            elif line.strip(" ").startswith("//") or line.strip(" ").startswith("#"):
                # This line is a comment.
                pass
    return header_list


if __name__ == "__main__":
    rpds_file = load_file("keys.rpds")
    print(rpds_file["NoKeys"])
    print(rpds_file["NoKeys"].docstring)
    print(rpds_file["NoKeys"]["0"])
    print(rpds_file["NoKeys"]["sheep"])
    print(rpds_file["NoKeys"]["1"])
    print(rpds_file["NoKeys"]["2"])
    print(rpds_file["NoKeys"]["crab"])
