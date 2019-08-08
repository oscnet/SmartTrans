#!/usr/bin/env python
# coding:utf-8

from googletrans import Translator
import codecs
import sys
import traceback

proxy = {
    'http': 'http://127.0.0.1:1086',
    'https': 'http://127.0.0.1:1086',
}

translator = Translator(proxies=proxy)

# translator.translate('# this is a test')

translate_batch_size = 50

file_input = str(sys.argv[1])
print(file_input)

file_output = "output.md"


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def require_translate(s):
    return s and not s.startswith("[") and not s.startswith("!") and not s.startswith("{")


with codecs.open(file_input, 'r', encoding='utf8') as fi:
    content = fi.readlines()

    content = [x.strip() for x in content]

    source_items = []
    translated_items = []

    # read input

    for line in content:
        if len(line) > 0:
            # source_items.append(line.encode(encoding='UTF-8'))
            source_items.append(line)

    # print(source_items)
    # split into batches
    # source_item_chunks = chunks(source_items, translate_batch_size)

    with codecs.open(file_output, 'w', encoding='utf-8') as fo:
        for s in source_items:
            # do translate
            fo.write(s.strip() + "\n")
            if (require_translate(s)):
                try:
                    t = translator.translate(s, src="en", dest='zh-cn')
                    print('.', end='', flush=True)
                    fo.write("\n")  # extra line for markdown line break
                    fo.write(t.text.strip() + "\n\n")
                except Exception as e:
                    print('X', end='', flush=True)
                    continue
        print('\n')

    print("Translated. Please check output.md!")
