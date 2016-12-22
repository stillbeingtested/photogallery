import os
import csv
import datetime

from django.db import transaction

from .models import User, Photo, Tag

base_path = os.path.dirname(os.path.abspath(__file__))


@transaction.atomic
def populate_database():
    with open(os.path.join(base_path, "test_data/test-photo.csv")) as csvfile:
        data_reader = csv.reader(csvfile, delimiter=';')

        # skip the first row with titles
        next(data_reader)
        nrows_processed = 0
        for row in data_reader:
            nrows_processed += 1
            if nrows_processed % 1000 == 0:
                print('processed rows', nrows_processed)

            user_id, photo_url = int(row[0]), row[1]
            addition_date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")

            if not User.objects.filter(pk=user_id).exists():
                user = User.objects.create(id=user_id, name=user_id)
            else:
                user = User.objects.get(pk=user_id)

            Photo.objects.create(user=user, href=photo_url, created_date=addition_date)

        populate_tags()

def populate_tags():
    for i in range(100):
        tag_name = "tag_%i" % i
        Tag.objects.create(name=tag_name, is_blocking=(i%10 == 0))