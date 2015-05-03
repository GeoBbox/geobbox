# -*- coding: utf-8 -*-

"""
To run this:
python json_to_csv.py json/micro_sample

Then everything in micro_sample directory will turned into csvs and
placed into the csv directory in a folder with the same name -
example - micro_sample

"""
import csv
import json
import os
import sys

src = sys.argv[1]
out = sys.argv[2]

for the_file in os.listdir(src):
    file_path = os.path.join(src, the_file)
    print(file_path)
    input = open(file_path)

    with open(file_path) as f:
        content = f.read().splitlines()

    data = []
    for item in content[:10]:
        if item:
            d = json.loads(item)
            data.append(d)
        # else: it is a blank line, so we don't care

    new_file = the_file.split('.')[0] + '.csv'
    new_file_path = os.path.join(out, new_file)

    # make dir if it doens't exist
    os.makedirs(out, exist_ok=True)
    output = csv.writer(open(new_file_path, 'w'))

    print(data[0].keys())
    output.writerow(data[0].keys())
    for rec in data:
        output.writerow(rec.values())

    output.close()

    print(file_path)
