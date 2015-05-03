# -*- coding: utf-8 -*-

"""
To run this:
python json_to_csv.py json/micro_sample csv/micro_sample
python json_to_csv.py input output

Then everything in micro_sample directory will turned into csvs and
placed into the csv directory. If the folder in the csv directory doesn't
exist, it will be created.

"""
import csv
import json
import os
import sys
import time

from dateutil import parser

src = sys.argv[1]
out = sys.argv[2]


def convert_date(date):
    ''' Example input 'Mon Apr 27 22:35:53 +0000 2015' '''

    parsed_date = parser.parse(date)
    parsed_date = time.mktime(date.timetuple())
    return parsed_date

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

    keys = [
        'id_str',
        'coor_lat', 'coor_long', 'coorpt', 'coor_created', 'coor_whole',
        'geo_lat', 'geo_long', 'geo_type',
        'bbox', 'bbox_type', 'bbox_full_name', 'bbox_name', 'bbox_place_type',
        'timestamp_ms',
        'user_geo_able', 'user_id', 'user_location'
    ]
    output.writerow(keys)

    for rec in data:
        import pprint
        pprint.pprint(rec)

        id_str = rec.get('id_str')

        coor = coor_lat = coor_long = None
        coorpt = coor_created = coor_whole = None
        coor = rec.get('coordinates')
        if coor:
            coordinates = coor.get('coordinates')
            if coordinates:
                coor_lat = coordinates[0]
                coor_long = coordinates[1]

            coorpt = coor.get('type')
            coor_created = coor.get('created_at')
            coor_whole = coor.get('created_at')
            if coor_whole:
                coor_whole = convert_date(coor_whole)

        geo = geo_lat = geo_long = None
        geo = rec.get('geo')
        if geo:
            geo_coor = geo.get('coordinates')
            if geo_coor:
                geo_lat = geo_coor[0]
                geo_long = geo_coor[1]

            geo_type = geo.get('type')

        bbox = rec['place']['bounding_box'].get('coordinates')
        bbox_type = rec['place']['bounding_box'].get('type')
        bbox_full_name = rec['place']['bounding_box'].get('full_name')
        bbox_name = rec['place']['bounding_box'].get('name')
        bbox_place_type = rec['place']['bounding_box'].get('place_type')

        timestamp_ms = rec['timestamp_ms']

        user_geo_able = rec['user']['geo_enabled']
        user_id = rec['user']['id']
        user_location = rec['user']['location']

        row = [
            id_str,
            coor_lat, coor_long, coorpt, coor_created, coor_whole,
            geo_lat, geo_long, geo_type,
            bbox, bbox_type, bbox_full_name, bbox_name, bbox_place_type,
            timestamp_ms,
            user_geo_able, user_id, user_location
        ]

        row = [str(x) for x in row]
        print(row)
        output.writerow(row)

    print(file_path)
