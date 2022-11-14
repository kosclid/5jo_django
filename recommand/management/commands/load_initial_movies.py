from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
import csv
import re
from recommand.models import Movie


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open(
            "데이터완성본_id추가_중복제거_link.csv", encoding="utf8"
        ) as csv_file_sub_categories:
            rows = csv.reader(csv_file_sub_categories)
            next(rows, None)
            for row in rows:
                m_n = row[1]
                if "Borat" in m_n:
                    m_n = m_n.split(":")[0].strip()
                print(m_n)

                m_n = re.sub(r"[^\w]", " ", m_n)
                m_n = m_n.replace("'", "")
                m_n = m_n.replace("  ", " ")
                year = int(row[4])
                sech = m_n + "_" + str(year)

                image_path = (
                    settings.BASE_DIR
                    / "recommand"
                    / "assets"
                    / "poster"
                    / "{}.png".format(sech)
                )

                with image_path.open("rb") as f:
                    file = File(f)
                    movie = Movie()
                    movie.movie_id = int(row[0])
                    movie.movie_name = row[1]
                    movie.year = int(row[4])
                    movie.movie_dir = row[5]
                    movie.movie_act = row[6]
                    movie.movie_ger = row[7]
                    movie.movie_text = ""
                    movie.movie_poster.save(image_path.name, file, save=False)
                    movie.movie_link = row[14]
                    movie.save()
                print(m_n)
            print("end done")
