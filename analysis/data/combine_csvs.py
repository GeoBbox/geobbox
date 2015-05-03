# -*- coding: utf-8 -*-
"""
To run this file:
python combine_csvs.py csv/streaming/ csv/streaming.csv

Where...
python combine_csvs.py input_folder/ output_csv.csv
"""

import sys
from glob import glob

src = sys.argv[1]
out = sys.argv[2]

with open(out, 'a') as singleFile:
    for csv in glob(src + '*.csv'):
        for line in open(csv, 'r'):
            singleFile.write(line)
