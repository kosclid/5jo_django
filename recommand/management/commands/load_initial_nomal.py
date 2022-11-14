from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
import csv
import re
from recommand.models import Ost, Ost_nomal


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open("clusterdata.csv", encoding="utf8") as csv_file_sub_categories:
            rows = csv.reader(csv_file_sub_categories)
            next(rows, None)
            for row in rows:
                ost_nom = Ost_nomal()
                ost = Ost.objects.get(id=int(row[0]) + 1)
                ost_nom.ost_id = ost
                ost_nom.cluster = int(row[3])
                ost_nom.num_gern = float(row[4])
                ost_nom.num_mvdir = float(row[5])
                ost_nom.num_valence = float(row[6])
                ost_nom.num_acousticness = float(row[7])
                ost_nom.num_danceability = float(row[8])
                ost_nom.num_energy = float(row[9])
                ost_nom.num_loudness = float(row[10])
                ost_nom.num_tempo = float(row[11])
                ost_nom.save()
                print(row[0])
            print("end done")
