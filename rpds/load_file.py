#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""


def load_file(file: str):
    """Loads a given file."""
    with open(file, "r") as file_open:
        for line in file_open.readlines():
            line = line.strip("\n")
            if line.strip(" ").startswith("[") and line.endswith("]"):
                # The line is a header
                print("Header: {}".format(line.strip(" ")))
                header_name = line[line.index("name=") + 5:line.index(line[-1])]
                if "," in header_name:
                    header_name = header_name[0:header_name.index(",")]
                print("Header Name: {}".format(header_name))
                try:
                    header_type = line[line.index("type=") + 5:line.index(line[-1])]
                except ValueError:
                    header_type = "<string>"
                print("Header Type: {}".format(header_type))
                print("-----------------------------------------------------------------------------------------------")
            elif line.strip(" ").startswith("-"):
                # The line is an item
                try:
                    item_type = line[line.index("<"):line.index(">") + 1]
                except ValueError:
                    item_type = "<string>"
                print("Item Type: {}".format(item_type))
                try:
                    item_value = line[line.index(">") + 2:line.index(line[-1]) + 1].strip(" ")
                except ValueError:
                    item_value = line[line.index("-") + 1:line.index(line[-1]) + 1].strip(" ")
                print("Item Value: {}".format(item_value))
                print("-----------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    load_file("included_example.rpds")
