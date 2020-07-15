#! /usr/bin/env python3

import json

data_file = 'hanzi_to_pinyin.json'

file_handler = open(data_file, 'r')
mappings = json.load(file_handler)

converted_strings = []

input_str = input("Input: ")

for c in input_str:
    result = ''
    try:
        result = mappings[c]
    except KeyError as keyerr:
        result = c
    finally:
        converted_strings.append(result)

output = ''.join(converted_strings)
print(output)