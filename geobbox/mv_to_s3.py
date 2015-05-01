# -*- coding: utf-8 -*-

import os
import sys

from boto.s3.connection import S3Connection
from boto.s3.key import Key

bucket_name = 'geobbox'

AWS_KEY = sys.argv[1]
AWS_SECRET = sys.argv[2]
aws_connection = S3Connection(AWS_KEY, AWS_SECRET)
bucket = aws_connection.get_bucket(bucket_name)

src = "data/"
print('Uploading %s to Amazon S3 bucket %s' % (src, bucket_name))


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

k = Key(bucket)

for the_file in os.listdir(src):
    file_path = os.path.join(src, the_file)
    k.set_contents_from_filename(file_path,
        cb=percent_cb, num_cb=10)

    os.remove(file_path)
