#! /usr/bin/env python3

import json

input_file = 'Unihan_Readings.txt'
output_file_mandarin = 'hanzi_to_pinyin.json'
output_file_cantonese = 'hanzi_to_jyutping.json'

file_handler = open(input_file, 'r')
mapping_mandarin = {}
mapping_cantonese = {}

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

    # only get the Mandarin and Cantonese fields
    if field != 'kMandarin' and field != 'kCantonese':
        continue

    unicode_value = int(unicode_value_raw[2:], 16)
    han_character = chr(unicode_value)
    # .encode('utf-8')

    if field == 'kMandarin':
        mapping_mandarin[han_character] = definition
    elif field == 'kCantonese':
        mapping_cantonese[han_character] = definition

# For debugging purposes only:
# json_str = json.dumps(mapping_mandarin, ensure_ascii=False)
# print(json_str)

with open(output_file_mandarin, 'w') as json_file:
    json.dump(mapping_mandarin, json_file, ensure_ascii=False)

with open(output_file_cantonese, 'w') as json_file:
    json.dump(mapping_cantonese, json_file, ensure_ascii=False)