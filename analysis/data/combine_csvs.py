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

count = 0

with open(out, 'a') as singleFile:
    for csv in glob(src + '*.csv'):
        file_line_count = 0
        for line in open(csv, 'r'):
            if count == 0:
                singleFile.write(line)
                count += 1
            elif file_line_count == 0:
                if count == 1:
                    singleFile.write(line)
                file_line_count += 1
            else:
                singleFile.write(line)
