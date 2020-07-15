# unihan-to-pinyin
This is a simple script that generates a character to pinyin and jyutping mapping in JSON from the
Unihan database.

## Running the generation script
The generation script is `unihan_to_pinyin.py` and runs on Python 3.7 or later. Despite its name
implying it only generates pinyin, it actually generates both pinyin and jyutping output files.
The output format is JSON, and the respective outputs are generated to `hanzi_to_pinyin.json` and
`hanzi_to_jyutping.json`.

Data is taken from the Unihan database. It is available for download at http://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip

Place the `Unihan_Readings.txt` from the Unihan database file in the base directory of your local
copy of this repo.