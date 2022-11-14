from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
import csv
from recommand.models import Movie, Ost


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open("데이터완성본_id추가.csv", encoding="utf8") as csv_file_sub_categories:
            rows = csv.reader(csv_file_sub_categories)
            next(rows, None)
            n = 0
            for row in rows:
                image_path = (
                    settings.BASE_DIR
                    / "recommand"
                    / "assets"
                    / "grapy"
                    / "{}.png".format(n)
                )

                with image_path.open("rb") as f:
                    file = File(f)
                    ost = Ost()
                    mv_id = Movie.objects.get(movie_id=row[0])
                    ost.movie_id = mv_id
                    ost.ost_name = row[2]
                    ost.valence = row[8]
                    ost.acousticness = row[8]
                    ost.danceability = row[9]
                    ost.energy = row[10]
                    ost.loudness = row[11]
                    ost.tempo = row[12]
                    ost.rader_chart.save(image_path.name, file, save=False)
                    ost.save()
                print(row[0])
                n += 1
            print("end done")
