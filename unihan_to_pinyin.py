#! /usr/bin/env python3

import json

input_file = 'Unihan_Readings.txt'
output_file = 'hanzi_to_pinyin.json'

file_handler = open(input_file, 'r')
mapping = {}

for line in file_handler:
    # skip comments
    if line[0] == "#":
        continue

    # get rid of \n character at end of line
    line = line[:-1]
    try:
        unicode_value_raw, field, definition = line.split('\t')
    except ValueError as val_err:
        continue

    # only get the Mandarin fields
    if field != 'kMandarin':
        continue

    unicode_value = int(unicode_value_raw[2:], 16)
    han_character = chr(unicode_value)
    # .encode('utf-8')

    mapping[han_character] = definition

json_str = json.dumps(mapping, ensure_ascii=False)
print(json_str)

with open(output_file, 'w') as json_file:
    json.dump(mapping, json_file, ensure_ascii=False)