#!/usr/bin/python3
"""
Module add all args to apython list and
saves them to a file
"""
import sys


save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_frm_json = __import__('6-load_from_json_file').load_from_json_file

items_file = "add_item.json"

try:
    list_items = load_frm_json("add_item.json")
except FileNotFoundError:
    list_items = []

for i in range(1, len(sys.argv)):
    list_items.append(sys.argv[i])

save_to_json(list_items, items_file)
