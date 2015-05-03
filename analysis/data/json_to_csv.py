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
    parsed_date = time.mktime(parsed_date.timetuple())
    return parsed_date

count = 0

for the_file in os.listdir(src):

    if not the_file.split('.')[0].endswith('(2)'):

        file_path = os.path.join(src, the_file)
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
        print(new_file_path)

        # make dir if it doens't exist
        os.makedirs(out, exist_ok=True)
        csv_file = open(new_file_path, 'w')
        output = csv.writer(csv_file)

        keys = [
            'id_str',
            'coor_lat', 'coor_long', 'coorpt',
            'created', 'created_secs',
            'geo_lat', 'geo_long', 'geo_type',
            'bbox', 'bbox_type',
            'bbox_lat1', 'bbox_long1', 'bbox_lat2', 'bbox_long2',
            'bbox_full_name', 'bbox_city', 'bbox_state',
            'bbox_name', 'bbox_place_type',
            'timestamp_ms',
            'user_geo_able', 'user_id', 'user_location'
        ]

        output.writerow(keys)

        for rec in data:

            id_str = rec.get('id_str')

            coor = coor_lat = coor_long = None
            coorpt = coor_created = coor_whole = None
            coor = rec.get('coordinates')
            if coor:
                coordinates = coor.get('coordinates')
                if coordinates:
                    coor_lat = coordinates[1]
                    coor_long = coordinates[0]

                coorpt = coor.get('type')

            created = created_secs = None
            created = rec.get('created_at')
            if created:
                created_secs = convert_date(created)

            geo = geo_lat = geo_long = None
            geo = rec.get('geo')
            if geo:
                geo_coor = geo.get('coordinates')
                if geo_coor:
                    geo_lat = geo_coor[0]
                    geo_long = geo_coor[1]

                geo_type = geo.get('type')

            bbox = bbox_lat1 = bbox_lat2 = bbox_long1 = bbox_long2 = None
            bbox = rec['place']['bounding_box'].get('coordinates')
            if bbox:
                bbox_lat1 = bbox[0][0][1]
                bbox_long1 = bbox[0][0][0]
                bbox_lat2 = bbox[0][2][1]
                bbox_long2 = bbox[0][2][0]

            bbox_type = rec['place']['bounding_box'].get('type')

            bbox_full_name = bbox_city = bbox_state = None
            bbox_full_name = rec['place'].get('full_name')
            if bbox_full_name:
                name_split = bbox_full_name.split(',')
                name_split = [x.strip() for x in name_split]
                try:
                    if name_split[1] == 'USA':
                        bbox_city = None
                        bbox_state = name_split[0]
                    else:
                        bbox_city = name_split[0]
                        bbox_state = name_split[1]
                except IndexError:
                    bbox_city = None
                    bbox_state = None

            bbox_name = rec['place'].get('name')
            bbox_place_type = rec['place'].get('place_type')

            timestamp_ms = rec['timestamp_ms']

            user_geo_able = rec['user']['geo_enabled']
            user_id = rec['user']['id']
            user_location = rec['user']['location']

            row = [
                id_str,
                coor_lat, coor_long, coorpt,
                created, created_secs,
                geo_lat, geo_long, geo_type,
                bbox, bbox_type,
                bbox_lat1, bbox_long1, bbox_lat2, bbox_long2,
                bbox_full_name, bbox_city, bbox_state,
                bbox_name, bbox_place_type,
                timestamp_ms,
                user_geo_able, user_id, user_location
            ]

            row = [str(x) for x in row]

            output.writerow(row)
            count += 1

            if count % 100 == 0:
                print(count)

        csv_file.close()
