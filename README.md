# unihan-to-pinyin
This is a simple script that generates a character to pinyin and jyutping mapping in JSON from the
Unihan database.

## Running the generation script
The generation script is `generate_mappings.py` and runs on Python 3.7 or later. It generates both
pinyin and jyutping output files. The output format is JSON, and the respective outputs are placed
into `hanzi_to_pinyin.json` and `hanzi_to_jyutping.json`.

Data is taken from the Unihan database. It is available for download at http://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip

Place the `Unihan_Readings.txt` from the Unihan database file in the base directory of your local
copy of this repo.

## Using the data
It's as simple as loading your JSON file into memory and doing substitutions for each word.

An example that reads input from stdin and outputs into stdout is located at `hanzi_to_pinyin.py`.