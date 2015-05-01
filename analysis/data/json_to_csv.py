# -*- coding: utf-8 -*-

"""
To run this:
python json_to_csv.py json/micro_sample

Then everything in micro_sample directory will turned into csvs and
placed into the csv directory in a folder with the same name -
example - micro_sample

"""
import csv
import os
import sys

src = sys.argv[1]

for the_file in os.listdir(src):
    file_path = os.path.join(src, the_file)
    print(file_path)
    input = open(file_path)

    content = []
    with open(file_path) as f:
        content = [f.read().splitlines()]

    # TODO - Start here.
    new_file_path = os.path.join("csv/", the_file)
    output = csv.writer(open(new_file_path, 'w'))
    print(content[0][0])
    output.writerow(content[0].keys())
    for rec in content:
        output.writerow(rec.values())

    output.close()

    print(file_path)
